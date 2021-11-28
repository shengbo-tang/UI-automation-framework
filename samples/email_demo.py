#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/11/28 13:14
@File   : email_demo.py  
=================================================="""
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


smtp_server = 'smtp.163.com'
smtp_sender = 't975426031@163.com'
smtp_senderpassword = 'LLHGWXTZCDDGVYMW'
smtp_receiver = 'tang975426031@foxmail.com'
smtp_cc = 'tang975426031@foxmail.com'
smtp_subject = '禅道自动化测试报告'
smtp_body = '禅道自动化测试的结果'

# 邮件文本消息
msg = MIMEText(smtp_body, 'html', 'utf-8')  # 邮件消息对象
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['Cc'] = smtp_cc
msg['subject'] = smtp_subject

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender, password=smtp_senderpassword)
smtp.sendmail(smtp_sender, smtp_receiver.split(',')+smtp_cc.split(','), msg.as_string())

