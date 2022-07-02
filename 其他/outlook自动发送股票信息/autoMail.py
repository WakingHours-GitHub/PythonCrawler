# pip install pywin32

import win32com.client as win32 # 直接导入win32 API
import datetime

def autoSend(message):
    print("调用")
    now_day = datetime.datetime.now().strftime("%m.%d") # 获取时间信息
    # print(now_day)

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    # 设置mail对象的各个属性

    mail.SentOnBehalfOfName = 'RemoteMessageSender@outlook.com'  # 选择发送邮箱,只需要修改对应使用的邮箱/账号地址即可
    mail.To = "WakingHoursHUC@outlook.com"  # 收件邮箱列表,如多人用;隔开
    # mail.CC = 'test@outlook.com'  # 抄送邮箱列表
    # mail.BCC = "test@outlook.com"  # 密抄邮箱列表，谨慎使用
    mail.Subject = f"400436 {now_day}号的价格信息"  # 邮件主题
    # mail.BodyFormat = 2
    mail.Body = message  # 邮件正文

    mail.Send() # 发送邮件

