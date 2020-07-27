#__author:  xiaoxinpro13
#date:  2020/7/27

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit(): #salary 是否像数字
    salary = int (salary)
# else:
#     print("salary must input digit")
#     exit("salary must input digit")

#print(name,age,job,salary)

msg =  '''
--------info of %s --------
Name : %s
Age: %d
Job: %s
Salary: %s
You will be retired %s years
------------end------------
''' % (name,name,age,job,salary,65-age)

print(msg)