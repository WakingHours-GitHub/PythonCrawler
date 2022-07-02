# 线程,进程
# 进程是资源单位,每一个进程至少要有一个线程
# 线程是执行单位

# 多线程程序中必须要有main函数, 代表其主线程
# 启动每一个程序默认都会右主线程, 默认都是main函数所在的线程

# 设置多线程的两种方式:
import threading
from threading import Thread  # 导入线程类


# 第一种开启线程的方式:
def fun():
    threading.current_thread().name = 'fun'
    for i in range(10000):

        print(threading.current_thread())
        print(i)


if __name__ == '__main__':
    t = Thread(target=fun())  # 将你要执行的函数传给新开辟的一个线程
    t.start()  # 标记多线程状态为可以开始工作状态,具体的执行时间由CPU决定
    threading.current_thread().name = 'main'

    # 主程序要干的事
    for i in range(1000):
        print(threading.current_thread())
        print(i)



# 另一种开启线程的方法
class MyThread(Thread):
    # 继承Thread类, 重写run方法, 当线程被strar时,默认执行的就是run方法
    def run(self):
        for i in range(1000):
            print(i)
if __name__ == '__main__':
    t = MyThread() # 创建对象
    t.start() # 标记为工作状态

    for i in range(10000):
        print(i)

