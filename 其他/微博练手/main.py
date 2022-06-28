import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.41",
    "referer": "https://s.weibo.com/weibo?q=p%27y%27t"
}


def research_requests():
    word = input("please input research words that you want to inquery: ")
    #
    # https://s.weibo.com/ajax/topsuggest.php?key=p%27y%27t&_k=1655554412178&_t=1&outjson=1&uid=0 # 原始数据, 但是我们使用地方中方式组合起来
    url = "https://s.weibo.com/ajax/topsuggest.php"
    params = {
        "key": word,
        "outjson": "1",
        "uid": "0",
    }
    resp = requests.get(url, headers=headers, params=params)
    print(resp.text)


    resp.close()

    def log_int_requests():
        log_in_url = "https://weibo.com/login.php"
        with requests.get(log_in_url, headers=headers) as resp:  # 使用任务管理器进行维护
            print(resp.text)


if __name__ == '__main__':
    # log_int_requests()
    research_requests()
