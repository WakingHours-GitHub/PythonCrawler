# import time
#
#
# def func():
#     print("我爱黎明")
#     time.sleep(3)  # 让当前的线程处于阻塞状态. CPU是不为我工作的
#     print("我真的爱黎明")
#
#
# if __name__ == '__main__':
#     func()
#
# """
# # input() 程序也是处于阻塞状态
# # requests.get(bilibili) 在网络请求返回数据之前, 程序也是处于阻塞状态的
# # 一般情况下, 当程序处于 IO操作的时候. 线程都会处于阻塞状态
#
# # 协程: 当程序遇见了IO操作的时候. 可以选择性的切换到其他任务上.
# # 在微观上是一个任务一个任务的进行切换. 切换条件一般就是IO操作
# # 在宏观上,我们能看到的其实是多个任务一起在执行
# # 多任务异步操作
#
# # 上方所讲的一切. 都是在单线程的条件下
# """


# python编写协程的程序
import asyncio
import time


# async def func():
#     print("你好啊, 我叫赛利亚")
#
#
# if __name__ == '__main__':
#     g = func()  # 此时的函数是异步协程函数. 此时函数执行得到的是一个协程对象
#     # print(g)
#     asyncio.run(g)  # 协程程序运行需要asyncio模块的支持



# async def func1():
#     print("你好啊, 我叫潘金莲")
#     # time.sleep(3)  # 当程序出现了同步操作的时候. 异步就中断了
#     await asyncio.sleep(3)  # 异步操作的代码
#     print("你好啊, 我叫潘金莲")
#
#
# async def func2():
#     print("你好啊, 我叫王建国")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("你好啊, 我叫王建国")
#
#
# async def func3():
#     print("你好啊, 我叫李雪琴")
#     await asyncio.sleep(4)
#     print("你好啊, 我叫李雪琴")
#
#
# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [
#         f1, f2, f3
#     ]
#     t1 = time.time()
#     # 一次性启动多个任务(协程)
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print(t2 - t1)


async def func1():
    print("你好啊, 我叫潘金莲")
    await asyncio.sleep(3)
    print("你好啊, 我叫潘金莲")


async def func2():
    print("你好啊, 我叫王建国")
    await asyncio.sleep(2)
    print("你好啊, 我叫王建国")


async def func3():
    print("你好啊, 我叫李雪琴")
    await asyncio.sleep(4)
    print("你好啊, 我叫李雪琴")


async def main():
    # 第一种写法
    # f1 = func1()
    # await f1  # 一般await挂起操作放在协程对象前面
    # 第二种写法(推荐)
    tasks = [
        asyncio.create_task(func1()),  # py3.8以后加上asyncio.create_task()
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    # 一次性启动多个任务(协程)
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)


# # 在爬虫领域的应用
# async def download(url):
#     print("准备开始下载")
#     await asyncio.sleep(2)  # 网络请求  requests.get()
#     print("下载完成")
#
#
# async def main():
#     urls = [
#         "http://www.baidu.com",
#         "http://www.bilibili.com",
#         "http://www.163.com"
#     ]
#
#     # 准备异步协程对象列表
#     tasks = []
#     for url in urls:
#         d = asycio.create_task(download(url))
#         tasks.append(d)
#
#     # tasks = [asyncio.create_task(download(url)) for url in urls]  # 这么干也行哦~
#
#     # 一次性把所有任务都执行
#     await asyncio.wait(tasks)
#
# if __name__ == '__main__':
#     asyncio.run(main())





