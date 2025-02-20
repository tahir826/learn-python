# name1 = "tahir hassan"
# name2 = 'tahir'
# age = 19
# name3 = '''bank details
# username 
# acc'''
# name4 = f''
# string1 = "tahir"
# string2 = "hassan"
# string3 = string1 + string2
# print(string3)
# num4 = 50
# def example(num1 , num2):
#     num3 = num1+ num2 + num4
#     return "tahir"


# print(example(20,30))
# num1 = 20
# num2 = 30

# if num1>num2:
#     print(f"{num1} is greater then {num2}")
# else:
#     print(f"{num1} is not greater then {num2}")
# num1 = int(input("enter your no. :- "))
# i = 1
# while i <= 10:
#     ans = num1*i
#     print(f"{num1} * {i} = {ans}")
#     i = i+1

# def example(num1,num2,num3):
#     num3=num1+num2
#     print(num3)

# example(20,30)


students = ["tahir","tayyab","ali"]
roll_no=[20,30,40]

# specific_student = students[2]
# print(specific_student)
# students.append("hassan")
input_user = input("enter student name :")
specific_index=students.index(input_user)
print(specific_index)
students.pop(1)

print(students)