
"""
# HTTP协议： url传输过程中遵循的的传输标准
这是表示在互联网中传输的数据, 遵循该协议.
协议: 就是两个计算机都遵循的一个协定, 常见的协议有TCP/IP, SOAP协议, HTTP协议...
HTTP: Hyper Text Transfer Protocol -> 超文本传输协议
超文本: 不止文本, 还有图片, 流媒体.

HTTP协议 将 一条消息分为三大块, 无论是请求还是响应都是三块内容
请求:
    请求行 -> 请求方式 请求URL地址 协议
        请求方式: 常用的两种方式: get; post
    请求头 -> 放一些服务器要使用的附加信息
        请求头里面放一些, 服务器需要(想要)知道的一些你的消息.
        那么如何你伪装的好, 就在请求头里面放一些伪装浏览器的内容, 即反反爬内容.
    请求体 -> 一般放一些请求参数
        请求的参数.

响应: 本地发送请求后, 服务器返回的响应
    状态行 -> 协议 状态码
        状态码:
            200: 成功
            404: 未找到
            500: 服务器问题
            302: 重定向
    响应头 -> 放一些客户端要使用的一些附加信息
        给客户端使用的附加信息. 例如cookie
    响应体 -> 服务器返回的真正的客户端要使用的内容(HTML, Json等)
        返回的内容.

请求头中最常见的一些重内容(爬虫需要)
    user_Agent: 用户标识, 请求载体的身份标识
    Referer: 防盗链 (这次请求是从那个页面中发来的? 反爬会用到)
    cookie: 本地字符串数据信(用户登陆信息, 反爬的token)

响应头中一些重要的内容:
    cookie: 本次字符串数据信息
    各种神奇的, 莫名其妙的字符串, (需要经验, 一般都是token字样, 防止各种攻击和反爬)

请求方式:
    get: 一般是查询的时候,    [显示提交]
    post: 增加, 修改, 上传,  [隐式提交]



"""