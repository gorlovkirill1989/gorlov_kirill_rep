# def add(*args, **kwargs):
#     def sum2(*args, **kwargs):
#         return x + y + z
#     return sum2
#
some = [1, 2, 3]
# summer = add(*some)
# print(summer(*some))


def triple_sum(a, b, c):
    return a + b + c


triple_sum(*some)
