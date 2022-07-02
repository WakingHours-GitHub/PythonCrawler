# 线程池的概念:
# 一次性开辟很多线程, 我们用户直接给线程池提交任务, 线程的任务调度, 交给线程池来完成
# 自己不用动手来去维护线程的空闲

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fun(name):
    for i in range(100000):
        print(name,i)

if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t: # 由系统自我调度
        for i in range(100): # 比如说有100个任务
            t.submit(fun, name = f"线程{i}")
    # 等待线程池中的任务全部执行完毕, 才能继续执行 # 称之为守护
    print("123")
