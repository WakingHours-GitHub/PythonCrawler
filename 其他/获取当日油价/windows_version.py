from get_fuel_price import get_oil_price  # 导入函数
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage

SENDER = "WakingHoursHUC@outlook.com"
PASSWD = "sdbevmkehgntrrvf"
RECEIVER = ["WakingHoursHUC@outlook.com"]

def conversation(data:list) -> str:
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <table style="border: 2px red; font-size: 30px">
        <tr>
            <td>{data[0][0]}</td>
            <td>{data[0][1]}</td>
            <td>{data[0][2]}</td>
            <td>{data[0][3]}</td>
            <td>{data[0][4]}</td>
        </tr>
        <tr>
            <td>{data[1][0]}</td>
            <td>{data[1][1]}</td>
            <td>{data[1][2]}</td>
            <td>{data[1][3]}</td>
            <td>{data[1][4]}</td>
        </tr>

    </table>
</body>
</html>
    """




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