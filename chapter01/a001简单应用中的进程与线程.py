import os
import threading

print(f'当前进程id：{os.getpid()}')
total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'当前python程序，共有{total_threads}个线程')
print(f'当前线程名称：{thread_name}')
