import csv
import json

# my_text = ""
#
# with open('my_input.txt') as my_file:
#     while True:
#         line = my_file.readline()
#         print(type(line), line)
#         my_text += line
#
#         if not line:
#             break
#
# print('From file:', my_text)
#
# # Open in write mode
# # with open('my_output.txt', 'w') as my_file:
# #     my_file.write(my_text)
#
#
# # Open in append mode
# with open('my_output.txt', 'a') as my_file:
#     my_file.write('\n\n\n')
#     my_file.write(my_text)

my_students = []
header = ()
student_data = []

with open('my_input.csv') as csv_file:
    my_data = csv.reader(csv_file)

    for index, data in enumerate(my_data):
        if index == 0:
            header = data
        else:
            student_data.append(data)

my_students = [{key: value for key, value in zip(header, element)} for element in student_data]

print(my_students)

with open('my_output.json', 'w') as json_file:
    json_object = json.dumps(my_students)
    json_file.write(json_object)
