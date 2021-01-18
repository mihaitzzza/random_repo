# import random

# my_strings = ['ana', 'are', 'mere', [1, 2, 3, ['a', 'b', 'c']], 1, 2, 3, 4, 5, 6, 7, 8, 9]
#               0      1      2
#              -3     -2     -1
# print(type(my_strings))
# print(type(my_strings).__name__)
# print(my_strings)
# print(len(my_strings))
# print(my_strings[0])
# print(my_strings[1])
# print(my_strings[2])
# print(len(my_strings))
# print(my_strings[len(my_strings) - 1])
# print(my_strings[len(my_strings) - 2])
# print(my_strings[len(my_strings) - 3])
# print(my_strings[len(my_strings) - 4])
# print(my_strings[len(my_strings) - 5])
# print(my_strings[len(my_strings) - 6])
# print(my_strings[-1])
# print(my_strings[-2])
# print(my_strings[-3])
# list_inside_list = my_strings[3]
# print(list_inside_list[1])
# print(my_strings[3][3][2])
# print(my_strings[1])
# print(my_strings[-2])
# print(len('ana are mere!'))
# print('ana are mere!'[0])
# print('ana are mere!'[1])
# print('ana are mere!'[-1])
# print('ana are mere!'[-2])

# my_fruits = ['banane', 'mere', 'gutui', 'pere', 'capsuni', 'pomelo', 'lubenita']
#               0        1        2       3        4          5          6
#              -7        -6      -5      -4       -3         -2         -1
# print(my_fruits)

# new_list = my_fruits[1:-1:3]  # start_index (+) : end_index (-) : step
# new_list = my_fruits[1::]  # start_index (+) : end_index (-) : step
# new_list = my_fruits[-3::]  # start_index (+) : end_index (-) : step
# new_list = my_fruits[:3:]  # start_index (+) : end_index (-) : step
# new_list = my_fruits[:-5:]  # start_index (+) : end_index (-) : step
# new_list = my_fruits[::2]  # start_index (+) : end_index (-) : step
# new_list = my_fruits[::-2]  # start_index (+) : end_index (-) : step
# new_list = my_fruits[::-1]
# my_random_list = random.shuffle(my_fruits)
# print(my_random_list)
# print(my_fruits)

# my_fruits = ['banane', 'mere', 'gutui', 'pere', 'capsuni', 'pomelo', 'lubenita']
# reversed_list = my_fruits[::-1]
# print(reversed_list)
# print('my_fruits', my_fruits)

# my_list_from_string = list('ana are mere')
# print(my_list_from_string)

# a = [1, 2, 3]
# a.append(4)
# b = [1, 2, 3]
# # print(a is b)
# # print(a == b)
# # print(a)
# # print(b)
# a_length = len(a)
# a_length_condition = len(a) == 4
# # print(a_length_condition is True)
# print(a_length_condition is not False)

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)

# a = [1, 2, 3]
# a.append(4)
# b = [1, 2, 3]
# b.append(5)
# print(a is b)
# print(a)
# print(b)

# a = [1, 2, 3]
# b = a  # b = [1, 2, 3]
# a.append(4)
# b.append(5)
# print(a is b)
# print(a)
# print(b)

# my_tuple = ('a', 'b', 'c', 'c')
# print(my_tuple)
# print(type(my_tuple))
# print(type(my_tuple).__name__)
# print(my_tuple[::-1])
# my_list = [1, 2, 3, 'b', True, None]
# my_tuple = tuple('ana are mere')
# print(my_tuple)
# print(type(my_tuple))
# print(type(my_tuple).__name__)
# my_tuple = (1, 2, 3)
# my_list = list(my_tuple)
# print(my_list)
# print(type(my_list))
# print(type(my_list).__name__)

# my_tuple = (1, 2, 3)
# print(id(my_tuple))
# l = list(my_tuple)
# l.append(4)
# my_tuple = tuple(l)
# print(id(my_tuple))
# print(my_tuple)

# a = ['a', 'b', 'c']
# b = (1, 2, a)
# c = [1, 2, b]
# my_list = c
# tuple_from_list = my_list[-1]
# print(type(tuple_from_list))
# list_from_tuple = tuple_from_list[-1]
# list_from_tuple.append('d')
# print('my_list', my_list)
# print('list_from_tuple', list_from_tuple)

# my_list = [1, 2, 3]
# print(id(my_list))
# my_list[0] = 'a'
# print(my_list[0])
# print(my_list)
# print(id(my_list))

# my_list = [9]
# my_tuple = (5,)
# print(type(my_tuple))
# print(len(my_tuple))

# my_dict = {
#     'cheie': 'ana are mere 1',
#     1: 'valoare-aabc',
#     (1,): [1, 2, 3, 4],
#     3+5j: (1, 2, 3),
#     'dict_key': {'a': 2},
# }
# print(my_dict)
# my_dict['new_key'] = 127
# print(my_dict)
# my_dict['cheie'] = list(my_dict['cheie'])
# print(my_dict)
# del my_dict[1]
# print(my_dict)
# print(type(my_dict))
# print(type(my_dict).__name__)
# print(my_dict)
# dict_keys = my_dict.items()
# print(dict_keys)
# print(type(dict_keys))
#
# dict_keys_list = list(my_dict.items())
# print(dict_keys_list)
# print(type(dict_keys_list))
#
# first_key = dict_keys_list[0][0]
# first_value = dict_keys_list[0][1]
# print('fk', first_key)
# print('fv', first_value)

# student_1 = {
#     'first_name': 'Mihai',
#     'last_name': 'Vladu',
#     'age': 28
# }
# print(student_1)
#
# my_students = [{
#     'first_name': 'Mihai',
#     'last_name': 'Vladu',
#     'age': 28
# }, {
#     'first_name': 'Mihai 1',
#     'last_name': 'Vladu 1',
#     'age': 29
# }, {
#     'first_name': 'Mihai 2',
#     'last_name': 'Vladu 2',
#     'age': 30
# }]
# print('my_students', my_students)


# student_1 = {
#     'first_name': 'Mihai',
#     'last_name': 'Vladu',
#     'age': 28,
#     # 'address': 'abc'
# }
# # print(student_1['address'])
# print(student_1.get('address', 'N/A'))

# print('a' in 'python')
# print('a' not in 'python')
# print(1 in [1, 2, 3])
# print(1 not in [1, 2, 3])
# print(1 in (1, 2, 3))
# print(1 not in (1, 2, 3))

# student_1 = {
#     'first_name': 'Mihai',
#     'last_name': 'Vladu',
#     'age': 28,
#     # 'address': 'abc'
# }
# print('first_name' in student_1)  # print('first_name' in student_1.keys())
# print('Mihai' in student_1.values())

my_set = {1, 2}
my_dict = {'a': 1}
print(type(my_set))
print(type(my_dict))
