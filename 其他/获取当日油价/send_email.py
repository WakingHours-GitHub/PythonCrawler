from get_fuel_price import get_oil_price  # 导入函数
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage

SENDER = "RemoteSender@outlook.com"
PASSWD = open("passwd.txt").read()
# print(PASSWD)
RECEIVER = ["WakingHoursHUC@outlook.com"]


def conversation(data: list) -> str:
    result_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        h1 {
            text-align: center;
            align-items: center;
            align-content: center;
        }

        table {
            border: 2px red solid;
            font-size: 20px;
            align-content: center;
            align-items: center;
            text-align: center;


        }
    </style>
</head>
<body>
<h1>今天油价！</h1>
<table cellpadding="10" align="center">
    <tr>
        <td>region</td>
        <td>#92</td>
        <td>#95</td>
        <td>#98</td>
        <td>update date</td>
    </tr>
    
    """
    end_str = """
</table>
</body>
</html>"""
    len(data)
    for i in range(len(data))[1:]:
        result_str += f"""
    <tr>
        <td>{data[i][0]}</td>
        <td>{data[i][1]}</td>
        <td>{data[i][2]}</td>
        <td>{data[i][3]}</td>
        <td>{data[i][4]}</td>
    </tr>
        """
    result_str += end_str
    # print(result_str)
    return result_str


def send_email(message: str, type: str) -> None:
    print("sending...")
    # 构建消息主题:
    email = MIMEText(message, "html", "utf-8")
    email["From"] = SENDER
    email["To"] = ','.join(RECEIVER)
    email["Subject"] = "Today Oil Price"
    with smtplib.SMTP("smtp.office365.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(SENDER, PASSWD)
        smtp.send_message(email)
    print("OK")


if __name__ == '__main__':
    # print(conversation(get_oil_price()))
    send_email(conversation(get_oil_price()), "html")
