"""
框架:
    能够简化劳动, 能够更少的代码做更强大的事情,
    是我们能更加专注于真正核心的代码, 避免简单, 重复劳动
    "不要重复造轮子"
Scrapy框架: 为了简化爬虫而生
Scrapy名声最大, 功能很强的一种框架

Scrapy框架概述:
    爬虫程序: 页面获取, 页面解析, 爬虫调度, 异常处理, 破解反爬
    Scrapy是基于Python的一个非常流行的网络爬虫框架.

    核心: 引擎(engine)
    然后有调度器, 蜘蛛程序, 下载器, 以及数据管道.
    过程: 首先是通过蜘蛛程序获取URL, 然后交给引擎, 引擎给到调度器,
    调度器会生成(维持)一个队列, 并且打标签(签名), 判断是否爬取. 然后将队列首, 交给引擎.
    引擎就会将这个请求, 给到下载器, 下载这个页面, 返回一个response对象. 给到引擎,
    然后引擎再给到蜘蛛程序, 将其解析页面, 蜘蛛程序将解析页面, 然后将解析好的数据打包成为一个item对象
    返回给引擎, 引擎再交给数据管道, 对其进行数据持久化.

    中间件: middleware:
    再Scrapy中有两个中间件:
        下载中间件:
            比如对requests设置代理, 或者对response预处理.
        蜘蛛中间件:
            拦截. 处理.

    我们要写的, 最核心的就是蜘蛛程序.
        种子URL, 以及页面解析部分.

    Scrapy组件:


安装和使用Scrapy
    更改全局镜像网站:
    pip config set global.index-url ...(源)

    pip install scrapy
    pip install -U scrapy # 更新安装
    pip install --user scrapy # 用户安装, 磁盘权限冲突时使用

    在命令行中使用scrapy命令创建名为demo的项目.
    输入scrapy, 可以查看帮助命令
    scrapy startproject 项目名 # 默认在当前目录下创建
    我们需要关注: spiders文件夹, 这是我们将来写蜘蛛程序的地方
    # 创建蜘蛛程序:
    scrapy genspider 名字 网站


    这种方式是在全局方式装的.
    我们工作中一般是每个项目不同的虚拟环境. 因此再创建好项目后, 我们再虚拟环境中可以选择再装一次
    当然, 这取决与你的解释器设置.


创建Scrapy项目

编写蜘蛛程序(核心):

编写数据管道:
    支持存储数据到csv, Excel, MySql等

编写中间件:
    模拟身份, 维持cookie




"""