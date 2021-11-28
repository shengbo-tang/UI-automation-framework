#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/11/28 14:31
@File   : email_demo2.py  
=================================================="""
import os.path
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from common.email_utils import MIMEMultipart


current_path = os.path.dirname(__file__)
smtp_file_path = os.path.join(current_path, '..', 'reports/禅道UI自动化测试报告V1.3.rar')


smtp_server = 'smtp.163.com'
smtp_sender = 't975426031@163.com'
smtp_senderpassword = 'LLHGWXTZCDDGVYMW'
smtp_receiver = 'tang975426031@foxmail.com'
smtp_cc = 'tang975426031@foxmail.com'
smtp_subject = '禅道自动化测试报告'
smtp_body = '禅道自动化测试的结果'
smtp_file = smtp_file_path

# 邮件文本消息
# msg = MIMEText(smtp_body, 'html', 'utf-8')  # 邮件消息对象
# msg['from'] = smtp_sender
# msg['to'] = smtp_receiver
# msg['Cc'] = smtp_cc
# msg['subject'] = smtp_subject

# 发压缩包邮件
msg = MIMEMultipart()
with open(smtp_file, 'rb') as f:
    mime = MIMEBase('zip', 'zip', filename=smtp_file.split('/')[-1])
    mime.add_header('Content-Disposition', 'attachment',
                    filename=('gb2312', '', smtp_file.split('/')[-1]))
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
msg.attach(MIMEText(smtp_body, "html", "utf-8"))
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['Cc'] = smtp_cc
msg['subject'] = smtp_subject

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender, password=smtp_senderpassword)
smtp.sendmail(smtp_sender, smtp_receiver.split(',')+smtp_cc.split(','), msg.as_string())