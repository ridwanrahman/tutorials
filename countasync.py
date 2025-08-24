"""
You use the async keyword to turn count() into a coroutine function that prints One,
waits for one second, then prints Two, and waits another second. You use the await keyword
to await the execution of asyncio.sleep(). This gives the control back to the program's event loop,
saying: I will sleep for one second. Go ahead and run something else in the meantime.

Coroutine: In python, a coroutine is a special type of function that can be paused during its execution and
then resumed later from the point where it was paused.
Coroutines can be entered, exited and resumed at many different points. It's the object you get
when you call a coroutine function.

Event Loop: It is the main scheduling mechanism that can handle and manage multiple tasks in a
single thread. It is the heart of the asyncio library in python, which is used for writing
single threaded concurrent code using coroutines.

Multiplexer: it notifies the event loop about an I/O events.
"""

import time
import asyncio

async def count():
    print("ONE")
    await asyncio.sleep(1)
    print("TWO")
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:.3f} seconds")
