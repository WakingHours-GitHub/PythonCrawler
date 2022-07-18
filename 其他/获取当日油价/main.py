from get_fuel_price import get_oil_price
from send_email import send_email, conversation
import os


def main() -> None:
    is_change = False
    lines = None
    oil_price_list2list = get_oil_price() # 获取最新油价.
    print(oil_price_list2list[1:]) # [['黑龙江', '8.74', '9.36', '10.62', '2022/7/15']]

    # 没有就写入
    if not os.path.exists("./data.txt"): # 如果没有文件, 则直接写入创建一个
        print("no directory, creat 'data.txt'")
        with open("./data.txt", "wt", encoding='utf-8') as f_write:
            for tr_list in oil_price_list2list:
                f_write.write(",".join(tr_list))
                f_write.write("\n")
        return  # 然后就返回

    with open("./data.txt", "r", encoding='utf-8') as f_read:
        lines = [x.strip().split(",") for x in f_read.readlines()[1:]] # 不要首行
        for i in range(len(lines)):
            if lines[i] != oil_price_list2list[i+1]:
                is_change = True
                break
        # for line, oil_list in lines, oil_price_list2list[1:]:
        #     if line != oil_list:
        #         is_change = True
        #         break

        # print(is_change)
        # 对比.
        if is_change:  # 只有油价改变时, 才发送邮件.
            print(lines) # [['黑龙江', '9.03', '9.67', '10.97', '2022/7/4']]

            for i in range(len(oil_price_list2list[1: ])): # 注意数组越界。
                for new_price, old_price in tuple(zip(oil_price_list2list[i+1], lines[i]))[1 :-1]:
                    # if new_price  old_price:
                    #     pass
                    print(new_price)
                    print(old_price)

            # return # 中断, 测试用


            # 发送邮件
            print("oil price change, send email")
            send_email(conversation(oil_price_list2list), "html")
            # 更新到文件当中
            with open("data.txt", "wt", encoding='utf-8') as f_write:
                for tr_list in oil_price_list2list:
                    f_write.write(",".join(tr_list))
                    f_write.write("\n")
        else:
            print("no any change, so don't send email")



if __name__ == '__main__':
    main()