# 用户手动登录： 得到cookie
# 带着cookie,去请求到个人页面的url -> 得到我们想要的内容

# 但是我们必须要将上面的两个操作炼连起来(连续的动作, 不能分开请求)
# 我们可以使用session进行请求 -> session 你可以认为是一连串的请求, 在这个过程中的cookie不会丢失
# 所以使用session就可以很好的满足了我们连续请求的要求
from 其他.获取chatset import getChatset
import requests
import re

# session 会话
session = requests.session() # 返回一个session对象, 用这个get或者post不会断

url = "https://github.com/WakingHours-GitHub" # 个人页面
resp = session.get(url)
# resp.encoding=re.search(r'charset="(?P<charset>.*?)"',resp.text).group("charset")
resp.encoding=getChatset(resp.text)
print(resp.text)

resp.close()