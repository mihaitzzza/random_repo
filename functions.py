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

my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

for index, element in enumerate(my_list):
    if element % 2 == 0:
        # print(f'element {list_element} from position {index} is even number')
        print(f'element {index + 1} with value {element} is even')
    elif element % 5 == 0:
        print(f'this is the last iteration! Current element: {element}')
        continue
    else:
        # print(f'element {list_element} from position {index} is odd number')
        print(f'element {index + 1} with value {element} is odd')

    print('----- BEFORE NEXT ITERATION!!!')

print('OUT OF FOR!')
