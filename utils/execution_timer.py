import time

class ExecutionTimer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.execution_time = self.end_time - self.start_time
        self.print_execution_time()

    def print_execution_time(self):
        hours, rem = divmod(self.execution_time, 3600)
        minutes, rem = divmod(rem, 60)
        seconds, milliseconds = divmod(rem, 1)
        milliseconds *= 1000
        print(f"Execution time: {int(hours)} hours, {int(minutes)} minutes, "
              f"{int(seconds)} seconds, {milliseconds:.4f} milliseconds")