# my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# list_length = len(my_list)

# if list_length % 2 == 0:
#     print('my list has even length')
#     if list_length % 3 == 0:
#         print('my list has even multiple of 3 length')
#     print('EVEN NEXT INSTRUCTION!')
# elif list_length % 5 == 0:
#     print('my list has odd length but is multiple of 5')
# else:
#     print('my list has odd length')
#
# print('FINAL NEXT INSTRUCTION')

# my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# list_length = len(my_list)
# index = 0  # [0, 1, 2, ... list_length - 1]
#
# # while index <= list_length - 1:  # 8 <= 9 (True) -> 9 <= 9 (True) -> 10 <= 9 (False)
# while index < list_length:  # 9 < 10 (True) -> 10 < 10(False)
#     list_element = my_list[index]
#
#     if list_element % 2 == 0:
#         # print(f'element {list_element} from position {index} is even number')
#         print(f'element {index + 1} with value {list_element} is even')
#     else:
#         # print(f'element {list_element} from position {index} is odd number')
#         print(f'element {index + 1} with value {list_element} is odd')
#
#     index += 1  # index = index + 1
#
# print('index', index)  # index will be list_length (index == list_length)

# my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]  # length: 10
#
# # for element in iterable:  # iterable can be tuple, list or any other iterable object.
# for index, element in enumerate(my_list):
#     if element % 2 == 0:
#         print(f'{element} from position {index} is even number')
#     else:
#         print(f'{element} from position {index} is odd number')

# my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]  # length: 10
# if len(my_list) % 2 != 0:
#     pass
# else:
#     print('even number')

# if len(my_list) % 2 == 0:
#     print('even number')

# my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# list_length = len(my_list)
# index = 0  # [0, 1, 2, ... list_length - 1]
#
# # while index <= list_length - 1:  # 8 <= 9 (True) -> 9 <= 9 (True) -> 10 <= 9 (False)
# while index < list_length:  # 9 < 10 (True) -> 10 < 10(False)
#     list_element = my_list[index]
#
#     if list_element % 2 == 0:
#         # print(f'element {list_element} from position {index} is even number')
#         print(f'element {index + 1} with value {list_element} is even')
#     elif list_element % 5 == 0:
#         print(f'this is the last iteration! Current element: {list_element}')
#         continue
#     else:
#         # print(f'element {list_element} from position {index} is odd number')
#         print(f'element {index + 1} with value {list_element} is odd')
#
#     index += 1  # index = index + 1
#
# print('index', index)

# my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#
# for index, element in enumerate(my_list):
#     if element % 2 == 0:
#         # print(f'element {list_element} from position {index} is even number')
#         print(f'element {index + 1} with value {element} is even')
#     elif element % 5 == 0:
#         print(f'this is the last iteration! Current element: {element}')
#         continue
#     else:
#         # print(f'element {list_element} from position {index} is odd number')
#         print(f'element {index + 1} with value {element} is odd')
#
#     print('----- BEFORE NEXT ITERATION!!!')
#
# print('OUT OF FOR!')

# def sum_of_numbers(a, b):
#     return a + b
#
#
# def compare_numbers(a, b):
#     return a < b
#
#
# def view_sum_numbers(a, b):
#     print(f'sum of {a} and {b} is {a + b}')
#
#
# def view_numbers_comparison(a, b):
#     print(f'{a} < {b} results in {a < b}')
#
#
# nr_1 = 5
# nr_2 = 7
# my_sum = sum_of_numbers(nr_1, nr_2)  # my_sum = 12
# print('my_sum', my_sum)
# comparison_true = compare_numbers(nr_1, nr_2)  # True  (5 < 7)
# comparison_false = compare_numbers(nr_2, nr_1)  # False (7 < 5)
# print('comparison', comparison_true)
# print('comparison', comparison_false)
# view_sum_numbers(nr_1, nr_2)
# view_numbers_comparison(nr_1, nr_2)

# def sum_of_numbers(a, b, c=0, d=0, e=None):
#     my_sum = a + b + c + d
#     if e is None:
#         return my_sum
#
#     return my_sum + e
#
#
# print(sum_of_numbers(a=5, b=7))
# print(sum_of_numbers(a=5, b=7, c=10))
# print(sum_of_numbers(a=5, b=7, d=10, c=12))

# def sum_of_numbers(a, b, *args, first_kw=0, second_kw=0, **kwargs):
#     print('a', a, 'b', b, 'args', args, 'first_kw', first_kw, 'second_kw', second_kw, 'kwargs', kwargs)
#     print('\n')
#
#     my_sum = 0
#     for i in args:
#         my_sum += i
#
#     for i in kwargs.values():
#         my_sum += i
#
#     return my_sum
#
#
# s1 = sum_of_numbers(5, 7)
# print(s1)
# s2 = sum_of_numbers(5, 7, 1, first_kw=29)
# print(s2)
# s3 = sum_of_numbers(5, 7, 1, 2, first_kw=29, second_kw=30)
# print(s3)
# s4 = sum_of_numbers(5, 7, 1, 2, 3, -7, -3)
# print(s4)
# s5 = sum_of_numbers(5, 7, 1, 2, 3, 4, -3.5, 0)
# print(s5)


def recursive_sum(n):
    # stop condition
    if n == 0:
        return 0

    return n + recursive_sum(n - 1)
# return 5 + ( return 4 + ( return 3 + ( return 2 + ( return 1 + ( return 0 ) ) ) ) )


print(recursive_sum(5))  # 0 + 1 + 2 + 3 + 4 + 5 = 15
