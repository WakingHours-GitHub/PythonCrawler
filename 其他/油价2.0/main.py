import os
import sys
from typing import List
from get_fuel import SpiderFuelPrices
import smtplib
from email.mime.text import MIMEText

SENDER = "RemoteSender@outlook.com" # 发送邮箱
PASSWD = open("passwd.txt").read() # 读取密码.
# print(PASSWD)
RECEIVER = ["WakingHoursHUC@outlook.com"] # 接收邮箱



def construct_message(region_selected_information : list[list]) -> str:
    pass



def send_email(region_selected : list[list]) -> None:
    print("sending email...")
    # 创建message
    message = construct_message(region_selected)
    # 构建消息主题 -> 使用HTML创建消息主题
    email = MIMEText(message, 'html', 'utf-8') # 创建消息对象.
    email['From'] = SENDER
    email['To'] = RECEIVER
    email['Subject'] = 'Today Oil Price' # 主题

    # 开启smtp进行发送
    with smtplib.SMTP("smtp.office365.com", 587) as smtp:
        smtp.ehlo() # 向服务器标识用户身份
        smtp.starttls()
        smtp.login(SENDER, PASSWD) # 登录
        smtp.send_message(email) # 传入创建好的对象, 进行发送

    print("send done!")


def main() -> None:
    # ROOT = os.getcwd() # 获取执行脚本处的目录, 获取当前执行脚本的所在的目录.
    # 因此使用shell执行时, 是shell执行处的目录, 并非py脚本的目录
    # ROOT = sys.argv[0] # 这才是获取脚本的绝对地址, 到脚本文件, 因此需要定位到上级, 才是文件夹.
    ROOT = sys.argv[0].rsplit("/", 1)[0] # 定位到上级文件夹.
    # print(ROOT)

    # return

    # 自动解包.
    header, region_selected = SpiderFuelPrices().start_spider()
    # print(header)
    # print(region_selected)

    write_content = ','.join(header) + '\n'+'\n'.join([','.join(region) for region in region_selected])
    is_repetition = False
    # 文件操作:
    if not os.path.exists(ROOT + "./data.txt"):
        open(ROOT+"./data.txt", 'w', encoding="utf-8").close() # create file

    # 打开.
    with open(ROOT+"./data.txt", "r", encoding='utf-8') as f_read:
        read_content = f_read.read()
        is_repetition = (read_content == write_content) if True else False


    if not is_repetition: # repetition
        print("fuel price updating") # 油价正在更新

        f_split = lambda x: x.split('\n')[1: ] # 要1到最后. 不要
        # 此时*_content已经是列表类型了. 经过split
        read_content = f_split(read_content)
        write_content = f_split(write_content)
        # 计算每一行(每一行表示一个地区)的差价
        # calculate price change of each row where represent a different region
        for old_data, new_data in zip(read_content, write_content):
            # print(content) # ('黑龙江,8.39,8.99,10.20,2022/8/23 13:28:50', '黑龙江,8.39,8.99,10.20,2022/8/23 13:28:59')
            # calculate price different(change)
            price_change_92 = new_data[1] - old_data[1]
            price_change_95 = new_data[2] - old_data[2]
            price_change_98 = new_data[3] - old_data[3]





        return


        with open(ROOT + "./data.txt", 'w', encoding="utf-8") as f_write:
            f_write.write(','.join(header))
            for region in region_selected:
                f_write.write("\n"+','.join(region))

    else: # not repetition
        print("fuel price has been update") # 油价无需更新

    # 发送邮件
    send_email(region_selected)











if __name__ == '__main__':
    main()
    # send_email()