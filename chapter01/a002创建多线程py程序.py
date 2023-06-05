import threading


def hello_from_thread():
    print(f'hello, from thread {threading.currentThread().name}')


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_thread = threading.active_count()
thread_name = threading.current_thread().name

print(f'python is currently running {total_thread} threads')
print(f'the current thread is {thread_name}')

hello_thread.join()
