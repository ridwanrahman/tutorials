from contextlib import AbstractContextManager


class TrialContextManager(AbstractContextManager):
    def __init__(self):
        print("init function")
    
    def __enter__(self):
        print("__enter__")
        return super().__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__")
        return super().__exit__(exc_type, exc_value, traceback)


if __name__ == "__main__":
    with TrialContextManager() as abc:
        print("i hope the context manager runs")
    