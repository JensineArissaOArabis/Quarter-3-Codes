import os

os.system('cls')

student = []
student.append(input("Enter your name: "))
student.append(input("Enter your age: "))
student.append(input("Enter your favorite subject: "))

print("\nStudent Record:")
print(f"Name: {student[0]}")
print(f"Age: {student[1]}")
print(f"Favorite Subject: {student[2]}")