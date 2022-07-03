# 1.拿到主页面的源代码. 然后提取到子页面的链接地址, href
# 2.通过href拿到子页面的内容. 从子页面中找到图片的下载地址 img -> src
# 3.下载图片
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = 'utf-8'  # 处理乱码

# print(resp.text)
# 把源代码交给bs
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_="TypeList").find_all("a")
# print(alist)
for a in alist:
    href = a.get('href')  # 直接通过get就可以拿到属性的值, 从标签中拿到某一属性, 直接通过get
    print(href)  # 打印出来了子页面的url

    # 拿到子页面的源代码
    child_page_resp = requests.get(href)  # 请求
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text  # 拿到页面源代码

    # 从子页面中拿到图片的下载路径(使用bs4)
    child_page = BeautifulSoup(child_page_text, "html.parser")
    p = child_page.find("p", align="center")  # 一般不适用align定位, 一般是向外扩,使用<xxx class 或者 id来定位>
    img = p.find("img")  # 从p标签找img
    src = img.get("src")  # 获取src, src中就是图片的url

    # 下载图片
    img_resp = requests.get(src)  # 请求大图的地址
    # 直接从请求中拿到图片
    # img_resp.content  # 这里拿到的是字节
    # 将所有获取得到的字节写入一个文件里面去, 那不就是图片吗
    img_name = src.split("/")[-1]  # 通过split('/')来切割,返回一个列表, 然后加上截取[-1]:拿到url中的最后一个/以后的内容
    with open("img/" + img_name, mode="wb") as f:
        f.write(img_resp.content)  # 图片内容写入文件
    child_page_resp.close()
    print("over!!!", img_name)
    time.sleep(1)  # 保证程序不要连续请求, 以防止服务器封IP

resp.close()  # 关闭

print("all over!!!")


# 最后一点想说明的是pycharm中会一直编码索引
# 这会极大的拖慢我们的运行速度
# 所以我们可以右键点击[将对象标记为][已排除]
# 此时已排除的文件夹pycharm不会索引
