# What is a context manager?
A python context manager is an object that defines what happens when you enter
and exit a with statement. It's a way to ensure that setup and cleanup code runs automatically.

It handles the entry into, and exit from, the desired runtime context for the execution of the block of code. 
Typical uses of context managers include saving and restoring various kinds of global state, lockign and unlocking resources, closing opened files, etc.