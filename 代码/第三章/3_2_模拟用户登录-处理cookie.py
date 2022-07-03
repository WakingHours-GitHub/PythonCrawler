# 登录 -> 得到cookie
# 带着cookie 去请求到书架url -> 书架上的内容

# 必须得把上面的两个操作连起来(连续的动作).
# 我们可以使用session进行请求 -> session你可以认为是一连串的请求. 在这个过程中的cookie不会丢失
# 这就很好的满足了我们连贯的请求的要求
import requests

# # 会话
# session = requests.session()
# data = {
#     "loginName": "18614075987",
#     "password": "q6035945"
# }
#
# # 1. 登录
# url = "https://passport.17k.com/ck/user/login"
# 看一下是否请求到了
# session.post(url, data=data) # 请求login获取到cooking
# # print(resp.text)
# # print(resp.cookies)  # 看cookie
# cookie看不到的, 勾选network下的保留日志: preserve log
#
# # 2. 拿书架上的数据
# # 刚才的那个session中是有cookie的， 然后再访问
# resp = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
#
# print(resp.json())

# 你也可以手动登录， 然后再network里找到cooking 然后手动复制下来
resp = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919", headers={
    "Cookie":"GUID=bbb5f65a-2fa2-40a0-ac87-49840eae4ad1; c_channel=0; c_csc=web; UM_distinctid=17700bddefba54-0a914fc70f1ede-326d7006-1fa400-17700bddefc9e3; Hm_lvt_9793f42b498361373512340937deb2a0=1614327827; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F16%252F16%252F64%252F75836416.jpg-88x88%253Fv%253D1610625030000%26id%3D75836416%26nickname%3D%25E9%25BA%25BB%25E8%25BE%25A3%25E5%2587%25A0%25E4%25B8%259D%26e%3D1629888002%26s%3D63b8b7687fc8a717; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2275836416%22%2C%22%24device_id%22%3A%2217700ba9c71257-035a42ce449776-326d7006-2073600-17700ba9c728de%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22bbb5f65a-2fa2-40a0-ac87-49840eae4ad1%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1614336271"
})
print(resp.text)

