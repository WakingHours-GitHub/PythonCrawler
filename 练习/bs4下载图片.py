import requests
from bs4 import BeautifulSoup


def main() -> None:
    # 主页面.
    main_url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",

    }
    # 注意, 使用https发送请求时, 我们需要去掉安全验证.
    resp = requests.get(main_url, headers=headers, verify=False)
    resp.encoding = "utf-8"  # 指定字符编码
    print(resp.text)

    # 将页面源代码放入到bs中进行解析:
    page = BeautifulSoup(resp.text, 'html.parser')
    page.find("")



    resp.close()


if __name__ == '__main__':
    main()
