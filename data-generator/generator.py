from faker import Faker
import csv
import numpy as np

fake = Faker()
mean_age = 40
age_sd = 10

with open('output-data/names.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['First Name', 'Last Name', 'Age'])
    
    for _ in range(10):
        name = fake.name().split()
        
        age = int(np.random.normal(mean_age, age_sd))
        age = max(18, min(age, 65))
        
        csv_writer.writerow([name[0], name[-1], age])
