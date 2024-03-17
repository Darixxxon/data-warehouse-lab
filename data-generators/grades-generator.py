from faker import Faker
import csv
import numpy as np

fake = Faker()

def get_grade_for_percentage(percentage):
    if percentage < 20:
        return 1
    elif percentage < 35:
        return 2
    elif percentage < 50:
        return 3
    elif percentage < 65:
        return 4
    elif percentage < 75:
        return 5
    elif percentage < 83:
        return 6
    elif percentage < 89:
        return 7
    elif percentage < 94:
        return 8
    elif percentage < 98:
        return 9
    else:
        return 10


options = [1, 2]
probabilities = [0.85, 0.15]


with open('output-data/grades.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['student_id', 'test_id', 'grade', 'percentage', 'attempt'])
    
    for i in range(1,451):
        student_id = i
        for j in range(1,51):
            test_id = np.random.randint(1, 400) #student nie pisze sobie randomowych testow tylko te ktore sa przypisane do jego kursow
            percentage = np.random.randint(1, 100)
            grade= get_grade_for_percentage(percentage)
            attempt = np.random.choice(options, p=probabilities)    #attempt jest troszke z dupy (ktos moze pisac tylko 2 xd)
            csv_writer.writerow([student_id, test_id, grade, percentage, attempt])