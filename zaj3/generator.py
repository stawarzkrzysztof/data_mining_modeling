import random
import csv
from faker import Faker

fake = Faker()
students_A = []
students_B = []
students_C = []

# generowanie danych uczniów
def generate_student_data(class_name):
    first_name = fake.first_name()
    last_name = fake.last_name()

    if class_name in ["A", "C"]:
        height = random.randint(150, 190)
    else:
        height = round(random.uniform(1.5, 1.9), 2)

    weight = random.randint(40, 120)
    if class_name in ["B", "C"] :
        weight = round(weight + random.random(), 1)

    return [first_name, last_name, height, weight]

# Generowanie danych dla klas A
for _ in range(random.randint(15, 25)):
    students_A.append(generate_student_data("A"))

# Generowanie danych dla klas B
for _ in range(random.randint(15, 25)):
    students_B.append(generate_student_data("B"))

# Generowanie danych dla klasy C
for _ in range(random.randint(15, 25)):
    students_C.append(generate_student_data("B"))

# Duplikacja rekordów z klasy A do klasy C
random_duplicates = random.sample(students_A, 3)
# Uwaga - do zagnieżdżonych struktur przy kopiowaniu należy użyć deepcopy - żeby nie zmieniało oryginałów
import copy
students_C += copy.deepcopy(random_duplicates)
last_three_students = students_C[-3:]
for student in last_three_students:
    student[2] = round(student[2] / 100, 2)
    student[3] = round(float(student[3]), 1)
students_C[-3:] = last_three_students
random.shuffle(students_C) # pomieszanie kolejnosci, żeby trudniej było zidentyfikować duplikaty

# Literówki w klasie C
random_typos = random.sample(range(len(students_C)), 3)
for index in random_typos:
    students_C[index][2] = 10 + students_C[index][2]

# Zły znak dziesiętny w klasie C
for student in students_C:
    for col in [2,3]:
        student[col] = str(student[col]).replace(".",",")

# Zapisz dane do plików CSV
with open('students_A.csv', 'w', newline='') as file_A, \
     open('students_B.csv', 'w', newline='') as file_B, \
     open('students_C.csv', 'w', newline='') as file_C:
    writer_A = csv.writer(file_A)
    writer_A.writerow(['First Name', 'Last Name', 'Height', 'Weight'])
    writer_A.writerows(students_A)

    writer_B = csv.writer(file_B)
    writer_B.writerow(['First Name', 'Last Name', 'Height (m)', 'Weight (kg)'])
    writer_B.writerows(students_B)

    writer_C = csv.writer(file_C, delimiter=';')
    writer_C.writerow(['Imie', 'Nazwisko', 'Wzrost (cm)', 'Waga (kg)'])
    writer_C.writerows(students_C)

print("Pliki CSV zostały wygenerowane.")