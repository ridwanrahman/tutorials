# What is a context manager?
A python context manager is an object that defines what happens when you enter
and exit a with statement. It's a way to ensure that setup and cleanup code runs automatically.

It handles the entry into, and exit from, the desired runtime context for the execution of the block of code. 
Typical uses of context managers include saving and restoring various kinds of global state, lockign and unlocking resources, closing opened files, etc.

A good mental model:
If you have an action that starts something -> you use it -> then it might closing/cleanup after.

### Use cases
1. file handling
File handling uses the concept of context managers a lot,. since you 

2. Database connections

3. Locking/Thread synchronization

4. Temporary state change

5. Measuring execution time

6. Network connections/Socket

7. Temporary Files/Directories

8. Resource Pooling

9. Mocking/Patching

