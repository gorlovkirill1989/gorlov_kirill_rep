from functools import wraps


# вспомогательная функция
def _log(message, filename=None):
    """Прокидывание файла"""
    if filename:
        with open(filename, "a") as file:
            print(message, file=file)
    else:
        print(message)


# декоратор логирования
def log(filename: str = ""):
    def my_decorator(func):
        """Декоратор логирования функций"""

        @wraps(func)
        def wrapper(*args, **kwargs):

            func_name = func.__name__

            try:
                result = func(*args, **kwargs)
                message = f"{func_name} ok"

                _log(message, filename)

                return result
            except Exception as e:
                message = f"{func_name} error: {e}. Inputs: {args}, {kwargs}"

                _log(message, filename)

                raise e

        return wrapper

    return my_decorator
