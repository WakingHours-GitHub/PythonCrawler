import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "2775753237"  # 用户名
mail_pass = "kgaturikiaopddja"  # 口令

sender = '2775753237@qq.com'
receivers = ['WakingHoursHUC@outlook.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText("""
工商银行: 1.45RMB
哈尔滨银行: 16RMB
""", 'plain', 'utf-8')
message['From'] = Header("WakingHours", 'utf-8')
message['To'] = Header("WakingHours", 'utf-8')

# subject = 'Python SMTP 邮件测试, 这是主题还是正文'
subject = """
账单
"""
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print(    "邮件发送成功")

except smtplib.SMTPException:
    print(    "Error: 无法发送邮件")