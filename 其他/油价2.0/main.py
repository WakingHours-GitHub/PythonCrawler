import copy
import gc
import os
import smtplib
import sys
from email.mime.text import MIMEText

from get_fuel import SpiderFuelPrices

SENDER = "RemoteSender@outlook.com"  # 发送邮箱
PASSWD = open("passwd.txt").read()  # 读取密码.
RECEIVER = ["WakingHoursHUC@outlook.com"]  # 接收邮箱
gc.collect()  # 垃圾回收


def construct_message(region_selected_information: list[list,]) -> str:
    # 数据格式: [['黑龙江', '8.23', '-0.160', '8.82', '-0.170', '10.00', '-0.200', '2022/8/24 15:48:49']]
    head = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <style type="text/css">
        table {
            margin: 0 0;
            padding: 0 0;
            align-content: center;
            border: 2px rgb(0, 0, 0) solid;
            font-size: 20px;
            align-content: center;
            align-items: center;
            text-align: center;
        }
    </style>

</head>


<body>
    <table>
        <tr>
            <th> 地区 </th>
            <th> 92号汽油 </th>
            <th> 较上次 </th>
            <th> 95号汽油 </th>
            <th> 较上次 </th>
            <th> 98号汽油 </th>
            <th> 较上次</th>
            <th> 更新日期 </th>
        </tr>
    """
    end = """
    </table>


</body>

</html>
    """
    content = """
            <tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>"""
    for region in region_selected_information:
        print(region)
        content.format(region[0], region[1], region[2], region[3], region[4], region[5], region[6], region[7])

    message = head + content + end
    print(message)
    return "test"

    # pass


def send_email(region_selected: list[list]) -> None:
    print("sending email...")
    print(region_selected)
    # 创建message
    message = construct_message(region_selected)
    return
    # 构建消息主题 -> 使用HTML创建消息主题
    email = MIMEText(message, 'html', 'utf-8')  # 创建消息对象.
    email['From'] = SENDER
    email['To'] = RECEIVER
    email['Subject'] = 'Today Oil Price'  # 主题

    # 开启smtp进行发送
    with smtplib.SMTP("smtp.office365.com", 587) as smtp:
        smtp.ehlo()  # 向服务器标识用户身份
        smtp.starttls()
        smtp.login(SENDER, PASSWD)  # 登录
        smtp.send_message(email)  # 传入创建好的对象, 进行发送

    print("send done!")


def main() -> None:
    # ROOT = os.getcwd() # 获取执行脚本处的目录, 获取当前执行脚本的所在的目录.
    # 因此使用shell执行时, 是shell执行处的目录, 并非py脚本的目录
    # ROOT = sys.argv[0] # 这才是获取脚本的绝对地址, 到脚本文件, 因此需要定位到上级, 才是文件夹.
    ROOT = sys.argv[0].rsplit("/", 1)[0]  # 定位到上级文件夹.
    # print(ROOT)

    # return

    # 自动解包.
    header, region_selected = SpiderFuelPrices().start_spider()  # 开启爬虫
    f_copy_function = lambda x: copy.deepcopy(x)

    header_copy = f_copy_function(header)
    region_selected_copy = f_copy_function(region_selected)

    # 对header处理:
    for i in range(2, 7, 2):
        header.insert(i, "较上次")

    print(header)
    print(header_copy)
    print(region_selected)

    # print(header)
    # print(region_selected)

    write_content = ','.join(header_copy) + '\n' + '\n'.join([','.join(region) for region in region_selected_copy])
    is_repetition = False
    # 文件操作:
    if not os.path.exists(ROOT + "./data.txt"):
        open(ROOT + "./data.txt", 'w', encoding="utf-8").close()  # create file

    # 打开.
    with open(ROOT + "./data.txt", "r", encoding='utf-8') as f_read:
        read_content = f_read.read()
        is_repetition = (read_content == write_content) if True else False

    if not is_repetition:  # repetition
        print("oil price updating")  # 油价正在更新
        k = 0

        f_split = lambda x: x.split('\n')[1:]  # 要1到最后. 不要head
        # 此时*_content已经是列表类型了. 经过split
        # 去除head
        read_content = f_split(read_content)
        write_content = f_split(write_content)

        # 计算每一行(每一行表示一个地区)的差价
        # calculate price change of each row where represent a different region
        for old_data, new_data in zip(read_content, write_content):
            # print(content) # ('黑龙江,8.39,8.99,10.20,2022/8/23 13:28:50', '黑龙江,8.39,8.99,10.20,2022/8/23 13:28:59')
            # calculate price different(change)
            new_data = new_data.split(',')
            old_data = old_data.split(',')

            price_change = list()  # 差价列表.
            for i in range(1, 4):
                price_change.append("{:.3f}".format((float(new_data[i]) - float(old_data[i]))))
            # price_change_92 = float(new_data[1]) - float(old_data[1])
            # price_change_95 = float(new_data[2]) - float(old_data[2])
            # price_change_98 = float(new_data[3]) - float(old_data[3])

            # (..._data\[.*?\])
            # float($1) 注意, 这里是使用$作为取分组的应用
            print(list(range(2, 7, 2)), price_change)

            # 这块有点不完美, 暂时没有想到好的解决方案.
            for index, value in zip(range(2, 7, 2), price_change):
                region_selected[k].insert(index, value.__str__())

            print(region_selected)
            k += 1

        # 只有油价更新, 才发送邮件
        send_email(region_selected)

        # return

        with open(ROOT + "./data.txt", 'w', encoding="utf-8") as f_write:
            f_write.write(','.join(header_copy))
            for region in region_selected_copy:
                f_write.write("\n" + ','.join(region))

    else:  # not repetition
        print("oil price has been update")  # 油价无需更新

    # 发送邮件


if __name__ == '__main__':
    main()
    # send_email()
