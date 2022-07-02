import smtplib
import os
assert 'SYSTEMROOT' in os.environ
# 用于构建 消息体
from email.message import EmailMessage
from email.mime.text import MIMEText
# 用于数据加密:
import ssl

context = ssl.create_default_context()

# 构建消息体
SENDER = "RemoteMessageSender@outlook.com"
FROM = "WakingHoursHUC@outlook.com"
PASSWD = "sdbevmkehgntrrvf"

subject = "Python test email"
message = """
<h1> 你就是歌姬吧 </h1>
"""

# 创建消息对象
msg = MIMEText(message, "html", "utf-8")
msg['subject'] = subject
msg['From'] = SENDER
msg['To'] = FROM

with smtplib.SMTP("smtp.office365.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(SENDER, PASSWD)
    smtp.send_message(msg)
