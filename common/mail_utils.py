#!/usr/bin/python
# -*- coding: UTF-8 -*-  
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

from apps.order import models
 
my_sender='whbke@163.com'    # 发件人邮箱账号
my_pass = 'Wangyi198997'              # 发件人邮箱密码
my_receivers=['546878587@qq.com']      # 收件人邮箱账号，我这边发送给自己

def send_order_email(orderId, title):
    order_info = models.OrderInfo.objects.get(pk=orderId)
    order_list = models.OrderList.objects.filter(order_info=order_info).all()
    mail_msg = """
    <table>
        <tr>
            <td colspan="2"><h3>基本信息</h3></td>
        </tr>
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
    <table>
        <tr>
            <td colspan="2"><h3>商品列表</h3></td>
        </tr>
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
    mail_msg += "</table>"

        
    try:
        message = MIMEText(mail_msg, 'html', 'utf-8')
        message['From']=formataddr(("吃货集中营",my_sender))  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To']=','.join([formataddr(("送货员<{madd}>".format(madd=item), item)) for item in my_receivers])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        subject = '{title}-订单 {order_id}'.format(title=title, order_id=orderId)
        message['Subject'] = Header(subject, 'utf-8')
 
        server=smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, my_receivers, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功")
    except smtplib.SMTPException as ee:
        print(ee)
        print("Error: 无法发送邮件")

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
