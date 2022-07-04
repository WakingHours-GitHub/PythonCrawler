from get_fuel_price import get_oil_price
from send_email import send_email, conversation



def main() -> None:
    is_change = False
    oil_price_list2list = get_oil_price()
    # print(oil_price_list2list[1:])

    with open("data.txt", "r", encoding='utf-8') as f_read:
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

        if is_change: # 只有油价改变时, 才发送邮件.
            print("oil price change, send email")
            send_email(conversation(oil_price_list2list), "html")
            # 保存到文件当中
            with open("data.txt", "wt", encoding='utf-8') as f_write:
                for tr_list in oil_price_list2list:
                    f_write.write(",".join(tr_list))
                    f_write.write("\n")
        else:
            print("no any change, so don't send email")



if __name__ == '__main__':
    main()