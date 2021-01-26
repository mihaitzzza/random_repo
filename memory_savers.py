# a = lambda: 1
#
#
# print(id(a))
# print('---', id(lambda: 1), id(lambda x, y, z: x + y + z))
# print(id(a))
# print('---', id(lambda: 2))
# print(id(a))
# print('---', id(lambda: 'a'))
# print(id(a))
# print('---', id(lambda: (1, 2, 3)))
# print(id(a))


# my_list = [1, 6, -3, 5]
# # my_list.sort()
# my_sorted_list = sorted(my_list)
#
# print(my_list, my_sorted_list)


# my_students = [{
#     "first_name": "1",
#     "last_name": "1",
#     "grade": 7
# }, {
#     "first_name": "2",
#     "last_name": "2",
#     "grade": 6.55
# }, {
#     "first_name": "3",
#     "last_name": "3",
#     "grade": 8
# }, {
#     "first_name": "4",
#     "last_name": "4",
#     "grade": 10,
# }, {
#     "first_name": "5",
#     "last_name": "5",
#     "grade": 3.25
# }, {
#     "first_name": "5",
#     "last_name": "5",
#     "grade": 1.25
# }]
# my_students.sort(key=lambda my_student: my_student['grade'], reverse=True)
# my_sorted_students = sorted(my_students, key=lambda my_student: my_student['grade'], reverse=True)
# print(my_sorted_students)


# my_cars = [{
#     "real_hp": 10,
#     "original_hp": 15,
# }, {
#     "real_hp": 20,
#     "original_hp": 20,
# }, {
#     "original_hp": 40
# }]
# # my_sorted_cars = sorted(my_cars, key=lambda a: a.get('hp', 0), reverse=True)
# my_sorted_cars = sorted(my_cars, key=lambda a: a['real_hp'] if 'real_hp' in a else a['original_hp'], reverse=True)
# print(my_sorted_cars)

# key exists in dict: ket in dict

# def update_student(student):
#     student = student.copy()
#     student['full_name'] = '%s %s' % (student['first_name'], student['last_name'])
#     student['promoted'] = student['grade'] >= 7
#
#     return student
#
#
# my_students = [{
#     "first_name": "1",
#     "last_name": "1",
#     "grade": 7
# }, {
#     "first_name": "2",
#     "last_name": "2",
#     "grade": 6.55
# }, {
#     "first_name": "3",
#     "last_name": "3",
#     "grade": 8
# }, {
#     "first_name": "4",
#     "last_name": "4",
#     "grade": 10,
# }, {
#     "first_name": "5",
#     "last_name": "5",
#     "grade": 3.25
# }, {
#     "first_name": "6",
#     "last_name": "6",
#     "grade": 1.25
# }]
# # my_students = list(map(update_student, my_students))
# # print(my_students)
# my_students = map(update_student, my_students)
# for student in my_students:
#     print(student)

# initial_numbers = (1, 2, 3, 4, 5)
# other_numbers = map(lambda x: {"initial_number": x, "squared_number": x * 2} if x % 2 == 0 else [1, 2], initial_numbers)
# other_numbers = tuple(other_numbers)
# print(other_numbers, type(other_numbers))


# my_students = [{
#     "first_name": "1",
#     "last_name": "1",
#     "grade": 7
# }, {
#     "first_name": "2",
#     "last_name": "2",
#     "grade": 6.55
# }, {
#     "first_name": "3",
#     "last_name": "3",
#     "grade": 8
# }, {
#     "first_name": "4",
#     "last_name": "4",
#     "grade": 10,
# }, {
#     "first_name": "5",
#     "last_name": "5",
#     "grade": 3.25
# }, {
#     "first_name": "6",
#     "last_name": "6",
#     "grade": 1.25
# }]
# my_promoted_students = filter(lambda x: x.get('grade', 2) >= 7, my_students)
# my_promoted_students = list(my_promoted_students)
# print(my_promoted_students, type(my_promoted_students))

# initial_numbers = tuple(range(1, 10))
# even_numbers = filter(lambda x: x % 2 == 0, initial_numbers)
# even_numbers = tuple(even_numbers)
# print('even_numbers', even_numbers)
# odd_numbers = filter(lambda x: x % 2 == 1, initial_numbers)
# odd_numbers = tuple(odd_numbers)
# print('odd_numbers', odd_numbers)

# my_tuple = ('a', 'b', 'c')
# my_list = [1, 2, 3]
# my_dict = {}
# for a, b in zip(my_tuple, my_list):
#     my_dict[a] = b
# print(my_dict)

my_initial_numbers = list(range(1, 11))
print('my_initial_numbers', my_initial_numbers)
my_squared_numbers = [x ** 2 for x in my_initial_numbers]
print('my_squared_numbers', my_squared_numbers)
my_even_numbers = [x for x in my_initial_numbers if x % 2 == 0]
print('my_even_numbers', my_even_numbers)
my_odd_squared_numbers = [x ** 2 for x in my_initial_numbers if x % 2 == 1]
print('my_odd_squared_numbers', my_odd_squared_numbers)

my_keys = ('a', 'b', 'c')
my_values = [1, 2, 3]
my_dict = {key: value for key, value in zip(my_keys, my_values) if value % 2 == 0}
print('my_dict', type(my_dict), my_dict)
