from urllib import request, parse
import json
import hashlib
import base64

from apps.express.models import KdNiaoExpressConfig

query_url = 'http://api.kdniao.com/Ebusiness/EbusinessOrderHandle.aspx'


def get_express_info(order_express):
    cnf = KdNiaoExpressConfig.objects.all()
    if len(cnf) == 0:
        return None
    cnf = cnf[0]
    # 请求
    try:
        data = get_traces(query_url, cnf.appId, cnf.appKey, order_express.expressId, order_express.company.code)
        if not data['Success'] or not any(data['Traces']):
            return None
        state = data['State']
        state_str = "无轨迹"
        if state == "1":
            state_str = "已揽收"
        elif state == "2":
            state_str = "在途中"
        elif state == "3":
            state_str = "签收"
        elif state == "4":
            state_str = "问题件"
        traces_data = data['Traces']
        traces = []
        for item in traces_data:
            traces.append({
                'accept_time': item['AcceptTime'],
                'accept_station': item['AcceptStation']
            })
        return {
            'state': state,
            'traces': traces
        }
    except Exception as ee:
        print(ee)
        return None


def datasign(jsonstr, api_key):
    """将请求数据先进行MD5编码，再base64编码"""
    data = jsonstr + api_key
    m = hashlib.md5()
    m.update(data.encode("utf-8"))
    code_1 = m.hexdigest()
    code_2 = base64.b64encode(code_1.encode("utf-8"))
    return code_2


def sendpost(url, data):
    data = parse.urlencode(data).encode('utf-8')
    headers = {
        "Accept": "application/x-www-form-urlencoded;charset=utf-8",
        "Accept-Encoding": "utf-8"
    }
    req = request.Request(url, headers=headers, data=data)
    get_data = request.urlopen(req).read().decode("utf-8")
    return get_data


def get_traces(url, api_id, api_key, logistic_code, shipper_code):
    request_data1 = {
        "OrderCode": "",
        "ShipperCode": shipper_code,
        "LogisticCode": logistic_code,
        "IsHandleInfo": "0"}
    request_data2 = json.dumps(request_data1, sort_keys=True)
    data_sign = datasign(request_data2, api_key)
    post_data = {
        'RequestData': request_data2,
        'EBusinessID': api_id,
        'RequestType': '1002',
        'DataSign': data_sign,
        'DataType': '2'
    }
    json_data = sendpost(url, post_data)
    get_data = json.loads(json_data)
    return get_data
