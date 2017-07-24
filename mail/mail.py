# -*- coding:utf-8 -*-
# email负责构造邮件，smtplib负责发送邮件
from email.mime.text import MIMEText
from email.header import Header
import smtplib

sender = '498785213@qq.com'
receiver = 'xiaonancrystal@163.com'

subject = 'python email test'
smtpserver = 'smtp.qq.com'  #发送服务器
username = '498785213@qq.com'
password = 'vdonmdiuyilmbiai'

msg = MIMEText('hello','text','utf-8')
msg['subject'] = Header(subject,'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

#需要需要开启POP3/SMTP服务,这时163邮件会让我们设置客户端授权码，
##这个授权码替代上面代码部分的passwd即可成功发送邮件