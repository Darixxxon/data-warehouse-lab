from faker import Faker
import csv
import numpy as np
import uuid

fake = Faker()
mean_age = 40
age_sd = 10    

with open('output-data/people.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['id', 'first_name', 'last_name', 'age'])
    
    for _ in range(1000):
        id = uuid.uuid4()
        
        name = fake.name().split()
        
        age = int(np.random.normal(mean_age, age_sd))
        age = max(18, min(age, 65))
        
        csv_writer.writerow([id, name[0], name[-1], age])
