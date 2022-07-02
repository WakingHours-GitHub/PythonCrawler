from multiprocessing import Process
from threading import Thread

# 进程是一个资源单位
# 多个进程：


# def func():
#     for i in range(1000):
#         print("子进程", i)
#

# if __name__ == '__main__':
#     p = Process(target=func) # 利用Process函数开辟一个新进程
# 和开线程一样， 
#     p.start()
#     for i in range(1000):
#         print("主进程", i)



# 一个函数
def func(name):
    for i in range(1000):
        print(i)

if __name__ == '__main__':
    t1 = Thread(target=func, args=('周杰伦',)) # 注意：传递参数必须是元组类型的, 只有一个元素时,记得加',',否则会报错
    t1.start()

