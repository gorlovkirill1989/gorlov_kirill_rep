import pytest
from src.decorators import log


@log()
def divide(x, y):
    return x / y


def test_log_decorator(capsys):
    divide(10, 2)
    captured = capsys.readouterr()
    assert captured.out == "divide ok\n"

    with pytest.raises(Exception, match="division by zero"):
        divide(10, 0)
        captured = capsys.readouterr()
        assert captured.out == "divide error: ZeroDivisionError: division by zero, Inputs: (10, 0), {}\n"
