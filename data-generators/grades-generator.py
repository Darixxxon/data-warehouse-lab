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
probabilities = [0.95, 0.05]


with open('output-data/grades-2020.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    # csv_writer.writerow(['student_id', 'test_id', 'grade', 'percentage', 'attempt'])
    
    # #rok 2020
    for year in range(0, 4):
        for i in range(1 + (year*90),91 + (year*90)):
            student_id = i
            for j in range(201 - (50 + (year*50)), 201 - (year*50)):
                test_id = j
                percentage = np.random.randint(1, 100)
                grade= get_grade_for_percentage(percentage)
                csv_writer.writerow([student_id, test_id, grade, percentage, 1]) 
                attempt = np.random.choice(options, p=probabilities)
                if attempt == 2:
                    percentage = np.random.randint(1, 100)
                    grade= get_grade_for_percentage(percentage)
                    csv_writer.writerow([student_id, test_id, grade, percentage, 2])     
            
            
with open('output-data/grades-2021.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile)    
     #rok 2021
    for year in range(0, 4):
        for i in range(1 + (year*90),91 + (year*90)):
            student_id = i + 90
            for j in range(401 - (50 + (year*50)), 401 - (year*50)):
                test_id = j
                percentage = np.random.randint(1, 100)
                grade= get_grade_for_percentage(percentage)
                csv_writer.writerow([student_id, test_id, grade, percentage, 1])               
                attempt = np.random.choice(options, p=probabilities)
                if attempt == 2:
                    percentage = np.random.randint(1, 100)
                    grade= get_grade_for_percentage(percentage)
                    csv_writer.writerow([student_id, test_id, grade, percentage, 2])            
                    