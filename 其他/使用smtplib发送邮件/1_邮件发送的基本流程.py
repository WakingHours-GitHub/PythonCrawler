"""
smtplib和mail都属于python内置库.

smtplib邮件自动发送
SMTP: Simple Mail Transfer Protocol: 简单邮件传统协议

准备需要发送邮件的邮箱账号:
    准备好发送的邮箱, 邮件从哪里发出.
    准备邮箱和密码, 有些邮箱第三方使用则需要授权码

发送邮件的基本步骤:
    1. 登陆邮件




"""

# 邮件发送的基本流程:
import smtplib
# 创建邮件对象, 真正被发送的对象
from email.mime.multipart import MIMEMultipart
# 邮件的主题:
from email.header import Header
# 构建文本内容
from email.mime.text import MIMEText

SENDER = "WakingHoursHUC@outlook.com"

# 1. 链接服务器, 登陆邮箱
# 根据不同的邮箱, 有不同的smtp服务器地址.
# smtplib.SMTP() # 也表示链接服务器, 但是无安全机制
# 写对应的smtp服务器地址: smtp.邮箱类型名.com
# 端口号: 使用邮箱应用的: 465/25
# 根据, 不同的邮箱.
# 链接对象 = smtplib.SMTP_SSL(smtp服务器地址, 端口号)
# 返回一个链接对象, 后续的所有操作都是在这个链接中进行.

connect = smtplib.SMTP("smtp.office365.com", 587) # 使用该种方式: 不会有垃圾邮件的提示. SSL是一个安全套接字,

connect.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
connect.starttls()

# 登陆邮箱
# 通过返回的链接对象.login(账号, 密码(授权码)) 进行登陆
# 使用outlook的密码. 记得做加密处理.
connect.login(SENDER, "sdbevmkehgntrrvf")

# 2. 编辑邮件: 准备数据
# 使用smtp发送邮件, 需要一个专门的email对象.
# 我们使用email对象, 将所有的发送相关的设置打包到一个对象, 然后直接使用stmp发送即可
# 2.1 创建对象
email = MIMEMultipart() # 创建对象
# 2.2 添加数据
# 设置邮件主题。
# Header(邮件标题, 编码方式)
subject = Header("发送邮件", "utf-8").encode() # 进行解码
# 添加到邮件对象当中
email["Subject"] = subject

# 其他对象同理:
# 设置邮件发送人
email["From"] = SENDER + "<"+SENDER+">"

# 设置邮件的接收人
# 收件人可以指定列表, 或者字符串用;分割多个收件人.
email["To"] = 'WakingHoursHUC@outlook.com'

# 邮件的内容部分:
# 普通文本创建方式: MIMEText() 对象
# MIMEText(文字内容, 文本类型, 编码方式)
# 文本类型 -> plain(普通文字), html(超链接), base64(二进制文件)
text = MIMEText(
    "this is a test email by Python auto program",
    "plain", # 内容类型
    "utf-8" # 编码方式
) # 返回一个文本对象
# 添加到email中.
email.attach(text)




# 3. 发送邮件.
# 通过链接对象进行发送
# connect.sendmail(发件人, 收件人, 字符串类型的邮件对象)
connect.sendmail(SENDER, "WakingHoursHUC@outlook.com", email.as_string())


connect.quit() # 退出











