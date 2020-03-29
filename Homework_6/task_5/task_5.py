import csv

departments = set()  # a set of departments (uniques values)

max_salary = ''  # maximum salary
temp_var = 0  # temporary variable
temp_var2 = 0  # temporary variable

max_department_salary = {}  # maximum salaries per departments
max_person_salary = {}  # maximum salaries per department


with open('Department_List.csv') as f:  # open the original csv file
    for row in csv.DictReader(f):  # iterate through all csv lines

        # task 1
        departments.add(row['Department'])  # add unique Department values

        # task 2
        if int(row['Salary']) > temp_var:  # compare row Salary value  with temporary variable
            max_salary = row['Salary']  # write max Salary
            temp_var = int(row['Salary'])

        # task 3/4
        if not row['Department'] in max_department_salary:  # check whether Department is in list
            max_department_salary[row['Department']] = int(row['Salary'])  # add Salary to the Department
            max_person_salary[row['Department']] = [row['Salary'], row['Last Name']]
            temp_var2 = int(row['Salary'])

        elif row['Department'] in max_department_salary and int(row['Salary']) > temp_var2:
            max_department_salary[row['Department']] = int(row['Salary'])
            max_person_salary[row['Department']] = [row['Salary'], row['Last Name']]

dep_quantity = len(departments)


with open('output.txt', 'w') as output:
    output.write(f'{dep_quantity}\n{max_salary}\n{max_department_salary}\n{max_person_salary}')
