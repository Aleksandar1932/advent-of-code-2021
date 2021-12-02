import typing

def print_result(task:int, result) -> typing.Callable:
    print(f"Task {task}:{result}")