# Student Performance Analyzer

print("==== Welcome to Student Performance Analyzer ====")


students=[]
count = int(input("How many Students? - "))

for j in range(count):
# Student Info
  print(f"Enter details of Student{j+1} : ")
  name = input("Enter Name : ")
  roll = input("Enter Roll Number : ")
  grade=''
  marks=[]


# Marks input
  print("Enter below marks for 2 subjects ->")

  for i in range(2):
    # marks=[]
    mark = int(input(f"Enter marks for Sub{i+1}: "))
    marks.append(mark)


  average =  round(sum(marks)/len(marks))


  # Grade Calculation
  if average >= 91:
    grade = "A+"

  elif average >= 81:
    grade = "A"

  elif average >= 71:
    grade = "B"

  elif average >= 61:
    grade = "C"

  elif average >= 51:
    grade = "D"

  elif average >= 40:
    grade = "E"

  else:
    grade = "Fail!!!"



  stud = {"name":name , "roll":roll , "average":average , "grade":grade, "marks":marks}
  students.append(stud)


# Report of Students
print("Report : ")

print("+----------+----------+----------+----------+----------+")
print('|    Name  | RollNo   | Average  | Grade    | Marks    |')
print("+----------+----------+----------+----------+----------+")
for s in students:
  print(f"|   {s['name']}    |   {s['roll']}    |   {s['average']}  |     {s['grade']}     |     {s['marks']}     |")
  print("+----------+----------+----------+----------+----------+")

top_avg = 0
class_avg=0
for s in students:
  class_avg+=s["average"]/len(students)
  

print(f"Class aaverage : {class_avg}")

topper = ''
for s in students:
  if top_avg < s['average'] : 
    top_avg = s['average']
    topper=s['name']

print(f"Topper : {topper} , Top Average : {top_avg}")
