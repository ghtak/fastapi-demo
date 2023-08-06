import asyncio
import threading


def run_sync(coro):
    class RunThread(threading.Thread):
        def __init__(self, coro_):
            self.coro = coro_
            self.result = None
            super().__init__()

        def run(self):
            self.result = asyncio.run(self.coro)

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None
    if loop and loop.is_running():
        thread = RunThread(coro)
        thread.start()
        thread.join()
        return thread.result
    else:
        return asyncio.run(coro)



#
# def run_async(func, *args, **kwargs):
#     class RunThread(threading.Thread):
#         def __init__(self, func, args, kwargs):
#             self.func = func
#             self.args = args
#             self.kwargs = kwargs
#             self.result = None
#             super().__init__()
#
#         def run(self):
#             self.result = asyncio.run(self.func(*self.args, **self.kwargs))
#
#     try:
#         loop = asyncio.get_running_loop()
#     except RuntimeError:
#         loop = None
#     if loop and loop.is_running():
#         thread = RunThread(func, args, kwargs)
#         thread.start()
#         thread.join()
#         return thread.result
#     else:
#         return asyncio.run(func(*args, **kwargs))
#
#
# loop = asyncio.get_running_loop()
# print(loop.is_running())

# run_async(init_models, container.engine())
