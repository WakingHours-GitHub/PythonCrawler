import os
import sys
from typing import List
from get_fuel import SpiderFuelPrices


def send_email(region_selected : list[list]) -> None:
    print(type(region_selected))






def main() -> None:
    # ROOT = os.getcwd() # 获取执行位置
    ROOT = sys.argv[0] # 这才是获取脚本的绝对地址, 到脚本文件, 因此需要定位到上级, 才是文件夹.
    ROOT = sys.argv[0].rsplit("/", 1)[0]
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

    with open(ROOT+"./data.txt", "r", encoding='utf-8') as f_read:
        content = f_read.read()
        is_repetition = content == write_content if True else False

    if not is_repetition: #
        print("fuel price updating") # 油价正在更新

        with open(ROOT + "./data.txt", 'w', encoding="utf-8") as f_write:
            f_write.write(','.join(header))
            for region in region_selected:
                f_write.write("\n"+','.join(region))
    else:
        print("fuel price has been update") # 油价无需更新

    # 发送邮件
    send_email(region_selected)











if __name__ == '__main__':
    main()
    # send_email()