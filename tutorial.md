# Async

Some definitions that are important:

1. Synchronous → means at the same time. 

It executes operations one by one, in a linear sequence. Where each step must complete and return a result before the next step is executed.

2. Asynchronous → means not at the same time. When programming, asynchronous means that the action is requested, although not performed at the same time of the request. it is performed later.
 
3. Non-blocking I/O → it is a way of performing I/O where reads and writes are requested, although performed asynchronously. The caller does not wait for the operation to complete before returning.

Performing I/O operations via asynchronous requests and responses, rather than waiting for operations to complete. NON-BLOCKING I/O IS IMPLEMENTED VIA ASYNCHRONOUS PROGRAMMING.

4. Asynchronous programming in python → refers to making requests in python and not blocking to wait for them to complete. 

5. Coroutine → function that can be paused during execution then resumed later from the point where it was paused.

6. Event loop → is the mechanism that handles and manages multiple tasks in a single thread. it runs on single thread. It provides concurrency via coroutines.


# Contextvars

Context variable is a way to share values between function and coroutines in python.

In concurrency, sharing state between different parts of the code is tricky. Context variables
help with that as it provides a simple and efficient way to manage, store and access context-local
state.