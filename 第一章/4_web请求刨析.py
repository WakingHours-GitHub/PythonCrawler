"""
Web请求全过程:

1. 服务器渲染：
    在服务器中统一直接把数据和html代码整合在一起, 统一返回给浏览器.
    在页面源代码中能够看到我们所请求的数据.
2. 客户端（浏览器）渲染： (本地渲染)
    第一次请求：服务器只返回一个html骨架。
    第二次请求：服务器返回数据，浏览器拿到数据进行数据展示
    数据和骨架在本地端（客户端）进行渲染, 最终呈现出来.
    在页面源代码中查看不到数据

那么对于在源代码中看不到数据的网站我们怎么实现爬虫.
那么浏览器渲染的方式，我们没办法看到数据，怎么办？
熟练的使用浏览器抓包工具：
可以F12看里面的内容：network（网络）查看里面的url请求
通过浏览器自带的抓包工具, 就可以看到所有的请求


"""
