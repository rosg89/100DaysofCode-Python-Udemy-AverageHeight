# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#Opcion rapida
""""
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)
"""


#Opcion larga

#Sumamos las alturas
total_height = 0
for height in student_heights:
  total_height += height

#Cuantos items hay en la list?
number_of_students = 0
for student in student_heights:
  number_of_students += 1

#Promedio y round
average_height = round(total_height / number_of_students)
print(f"The average height is {average_height}")