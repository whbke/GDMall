#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from apps.order import models
 
sender = 'whbke@163.com'
receivers = ['whbke@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 # 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="whbke@163.com"    #用户名
mail_pass=""   #口令 

def send_order_email(orderId, title):
    order_info = models.OrderInfo.objects.get(pk=orderId)
    order_list = models.OrderList.objects.filter(order_info=order_info).all()
    mail_msg = """
    <p>基本信息</p>
    <table>
        <tr>
            <td>订单地址：</td>
            <td>{address}</td>
        </tr>
        <tr>
            <td>联系电话：</td>
            <td>{phone}</td>
        </tr>
        <tr>
            <td>姓名：</td>
            <td>{name}</td>
        </tr>
        <tr>
            <td>订单总额：</td>
            <td>{total_price}</td>
        </tr>
    </table>
    """.format(address=order_info.address,
        phone=order_info.phone,
        name=order_info.name,
        total_price=order_info.total_price)
    mail_msg += """
    <p>基本信息</p>
    <table>
        <tr>
            <th>商品</th>
            <th>价格</th>
            <th>个数</th>
        </tr>
    """
    for item in order_list:
        mail_msg += '''
        <tr>
            <td>{name}</td>
            <td>{price}</td>
            <td>{count}</td>
        </tr>
        '''.format(
            name=item.commodity.name,
            price=item.commodity_price,
            count=item.commodity_count)

    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header("吃货集中营", 'utf-8')
    message['To'] =  Header("送货员", 'utf-8')

    subject = '<{title}>-订单 {order_id}'.format(title=title, order_id=orderId)
    message['Subject'] = Header(subject, 'utf-8')
        
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as ee:
        print(ee)
        print("Error: 无法发送邮件")