# 导入相关的库和方法
import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合并起来
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host = "smtp.outlook.com"
mail_sender = "RemoteMessageSender@outlook.com"
# mail_licence = ""
mail_receivers = ['WakingHoursHUC@outlook.com']

email = MIMEMultipart('related')

subject_content = "您的第一封py自动邮件"
email["From"] = "sender_name<WakingHoursHUC@outlook.com>"
email["To"] = "receiver_name<WakingHoursHUC@outlook.com>"
email["Subject"] = Header(subject_content, 'utf-8')


body_content = "这是Py自动发出的邮箱"
message_text = MIMEText(body_content, "plain","utf-8")
email.attach(message_text)

stp = smtplib.SMTP()
stp.connect(mail_host, 25)
stp.login(mail_sender, "FWJ@15246337585")

stp.sendmail(mail_sender, mail_receivers, email.as_string())
print('邮件发送成功')