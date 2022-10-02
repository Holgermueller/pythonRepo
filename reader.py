#employee_file = open('employess.txt', 'a')
employee_file = open('index.html', 'w')

# print(employee_file.readlines())
employee_file.write('<p>This is HTML</p>')


employee_file.close()
