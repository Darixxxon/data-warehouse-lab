import csv
import random

names_teacher = ["Aleksandra", "Wiktoria", "Emilia", "Laura", "Natalia", "Antonina", "Pola", "Lilianna", "Iga", 
         "Marcelina", "Anna", "Gabriela", "Helena", "Michalina", "Nadia", "Kornelia", "Milena", "Martyna", 
         "Klara", "Nikola", "Jagoda", "Barbara", "Karolina", "Agata", "Magdalena", "Jakub", "Mateusz", "Dawid"]

surnames_teacher = ["Nowak", "Kowalska", "Wisniewska", "Wojcik", "Kowalczyk", "Kaminska", "Lewandowska", "Zielinska", 
            "Szymanska", "Dabrowska", "Wozniak", "Kozlowska", "Mazur", "Jankowska", "Kwiatkowska", "Wojciechowska", 
            "Krawczyk", "Kaczmarek", "Piotrowska", "Grabowska"]

dates_teacher = ["1987-09-25", "1981-11-14", "1985-03-06", "1976-07-02", "1988-05-19", "1992-10-30", "1983-12-21", 
         "1989-04-11", "1980-08-09", "1975-01-18", "1993-06-28", "1974-09-23", "1972-12-05", "1977-02-15", 
         "1971-06-07", "1994-01-20", "1984-07-12", "1990-11-03", "1986-04-25", "1982-08-17", "1973-03-29", 
         "1991-09-07", "1979-05-31", "1978-10-13", "1987-08-04", "1988-12-26", "1970-02-24", "1995-03-16", 
         "1994-09-02", "1976-11-09"]

addresses_teacher = ["Gdynia Swietojanska 12", "Gdynia Starowiejska 45", "Gdynia Wladyslawa IV 78", "Gdynia Morska 13", 
             "Gdynia Legionow 21", "Gdynia 3 Maja 55", "Gdynia Wiejska 72", "Gdynia Armii Krajowej 91", 
             "Gdynia Wiczlina 5", "Gdynia Jana z Kolna 33", "Gdynia Akademicka 47", "Gdynia Pucka 69", 
             "Gdynia Swietokrzyska 87", "Gdynia Slowackiego 32", "Gdynia Kosciuszki 16", "Gdynia Abrahama 74", 
             "Gdynia Paderewskiego 39", "Gdynia Wzgorze Sw. Maksymiliana 90", "Gdynia Sobotki 25", "Gdynia Chwarznienska 17", 
             "Gdynia Chopina 66", "Gdynia Kaszubska 49", "Gdynia Marynarki Polskiej 23", "Gdynia Derdowskiego 84", 
             "Gdynia Powstania Styczniowego 18", "Gdynia Hutnicza 28", "Gdynia Kielecka 7", "Gdynia Polska 56", 
             "Gdynia Wzgorze Nawiedzenia 93", "Gdynia Komuny Paryskiej 9"]

working_since = ["2003-07-14", "2002-10-29", "2007-03-05", "2010-09-21", "2006-05-17", "2009-12-03", "2004-08-26", "2005-11-09", 
                 "2008-01-12", "2010-04-28", "2002-12-17", "2003-04-01", "2006-07-23", "2007-09-06", "2009-01-30", "2008-11-15", 
                 "2004-01-27", "2011-06-10", "2005-02-13", "2003-10-05", "2008-04-14", "2009-07-28", "2006-03-09", "2010-10-02", 
                 "2007-05-06", "2002-06-19", "2004-12-08", "2011-02-18", "2005-08-01", "2010-01-25"]

group_names = ["Little Ducks", "Tiny Tigers", "Happy Hippos", "Cheerful Chipmunks", "Colorful Caterpillars", "Playful Penguins", 
               "Giggly Giraffes", "Sunny Sunflowers", "Funny Frogs", "Busy Bees", "Merry Monkeys", "Whispering Whales", 
               "Sparkling Stars", "Curious Kittens", "Bouncing Bunnies"]

names_students = ["Antoni", "Jakub", "Jan", "Szymon", "Franciszek", "Filip", "Kacper", "Aleksander", "Mikolaj", "Wojciech", "Adam", 
                  "Stanislaw", "Michal", "Marcel", "Piotr", "Karol", "Mateusz", "Bartosz", "Wiktor", "Dominik", "Igor", "Hubert", 
                  "Dawid", "Oliwier", "Kamil", "Maciej", "Patryk", "Dariusz", "Tomasz", "Rafal", "Tymoteusz", "Blazej", "Damian", 
                  "Robert", "Grzegorz", "Krzysztof", "Norbert", "Sebastian", "Lukasz", "Arkadiusz", "Kornel", "Ksawery", "Ignacy", 
                  "Dawid", "Wiktor", "Mateusz", "Bartosz", "Piotr", "Adam", "Kacper", "Wojciech", "Michal", "Filip", "Antoni", "Jan", 
                  "Jakub", "Szymon", "Oliwier", "Dominik", "Karol", "Marcel", "Blazej", "Stanislaw", "Mikolaj", "Hubert", "Igor", 
                  "Tomasz", "Maciej", "Robert", "Dawid", "Patryk", "Rafal", "Kamil", "Norbert", "Grzegorz", "Krzysztof", "Tymoteusz", 
                  "Arkadiusz", "Damian", "Ignacy", "Kornel", "Sebastian", "Wiktor", "Bartosz", "Mateusz", "Piotr", "Adam", "Kacper", 
                  "Michal", "Jakub", "Antoni", "Szymon", "Jan", "Filip", "Wojciech", "Karol", "Marcel", "Dominik", "Oliwier", "Blazej", 
                  "Mikolaj", "Stanislaw", "Hubert", "Igor", "Wiktoria", "Zuzanna", "Maja", "Hanna", "Lena", "Amelia", "Aleksandra", 
                  "Natalia", "Julia", "Zofia", "Emilia", "Maria", "Anna", "Laura", "Martyna", "Oliwia", "Antonina", "Kinga", "Barbara", 
                  "Kamila", "Patrycja", "Magdalena", "Gabriela", "Karolina", "Monika", "Daria", "Blanka", "Paulina", "Nikola", "Agata", 
                  "Kornelia", "Justyna", "Weronika", "Klaudia", "Dominika", "Alicja", "Dorota", "Sara", "Wiktoria", "Natalia", "Julia", 
                  "Zuzanna", "Amelia", "Lena", "Hanna", "Maja", "Aleksandra", "Emilia", "Zofia", "Anna", "Martyna", "Laura", "Oliwia", 
                  "Patrycja", "Antonina", "Magdalena", "Gabriela", "Karolina", "Daria", "Kamila", "Barbara", "Blanka", "Kinga", "Monika", 
                  "Dominika", "Paulina", "Agata", "Klaudia", "Nikola", "Justyna", "Sara", "Weronika", "Kornelia", "Alicja", "Dorota"]

surnames_students = ["Nowak", "Kowalska", "Wisniewska", "Wojcik", "Kowalczyk", "Kaminska", "Lewandowska", "Zielinska", "Szymanska", 
                     "Dabrowska", "Wozniak", "Kozlowska", "Mazur", "Jankowska", "Kwiatkowska", "Wojciechowska", "Krawczyk", "Kaczmarek", 
                     "Piotrowska", "Grabowska", "Pawlowicz", "Michalska", "Adamczyk", "Zajac", "Nowicka", "Malinowska", "Przybylska", 
                     "Dudek", "Wieczorek", "Jablonska", "Krol", "Majewska", "Olszewska", "Jaworska", "Wrobel", "Witkowska", "Walczak", 
                     "Stepinska", "Gorska", "Michalak", "Szewczyk", "Sikora", "Ostrowska", "Baran", "Tomaszewska", "Zalewska", "Zawadzka", 
                     "Sawicka", "Kubiak", "Lis", "Sobczak", "Kowalik", "Mazurek", "Krajewska", "Ziolkowska", "Sobolewska", "Czarnecka", 
                     "Kaczmarczyk", "Wlodarczyk", "Borkowska", "Sadowska", "Sikorska", "Laskowska", "Brzezinska", "Baranowska", "Makowska", 
                     "Pawlak", "Zakrzewska", "Glowacka", "Witczak", "Wasilewska", "Marciniak", "Kubiak", "Kowalewska", "Dabrowska", 
                     "Blaszczyk", "Sobolewski", "Nowakowska", "Kaczor", "Urbaniak", "Wieczorek", "Klimek", "Duda", "Piotrowski", "Gajewska", 
                     "Leszczynska", "Pietrzak", "Mroz", "Maj", "Bednarczyk", "Sawicki", "Kurek", "Mazur", "Wasilewski"]

dates_students = ["2014-01-07", "2014-02-15", "2014-03-25", "2014-04-06", "2014-05-10", "2014-06-28", "2014-07-15", "2014-08-24", "2014-09-11", 
                  "2014-10-18", "2014-11-01", "2014-12-22", "2014-01-18", "2014-02-03", "2014-03-26", "2014-04-11", "2014-05-29", "2014-06-15", 
                  "2014-07-20", "2014-08-12", "2014-09-23", "2014-10-05", "2014-11-11", "2014-12-27", "2014-01-28", "2014-02-08", "2014-03-27", 
                  "2014-04-20", "2014-05-05", "2014-06-20", "2014-07-02", "2014-08-19", "2014-09-26", "2014-10-13", "2014-11-22", "2014-12-06", 
                  "2014-01-14", "2014-02-21", "2014-03-09", "2014-04-02", "2014-05-28", "2014-06-08", "2014-07-17", "2014-08-21", "2014-09-02", 
                  "2014-10-27", "2014-11-05", "2014-12-18", "2014-01-23", "2014-02-18", "2014-03-02", "2014-04-24", "2014-05-15", "2014-06-25", 
                  "2014-07-05", "2014-08-03", "2014-09-07", "2014-10-29", "2014-11-14", "2014-12-12", "2014-01-26", "2014-02-22", "2014-03-05", 
                  "2014-04-15", "2014-05-19", "2014-06-22", "2014-07-29", "2014-08-16", "2014-09-20", "2014-10-07", "2014-11-26", "2014-12-17", 
                  "2014-01-11", "2014-02-07", "2014-03-27", "2014-04-14", "2014-05-17", "2014-06-29", "2014-07-13", "2014-08-23", "2014-09-11", 
                  "2014-10-09", "2014-11-02", "2014-12-28", "2014-01-18", "2014-02-03", "2014-03-26", "2014-04-11", "2014-05-29", "2014-06-15", 
                  "2015-01-05", "2015-02-15", "2015-03-20", "2015-04-07", "2015-05-11", "2015-06-23", "2015-07-09", "2015-08-29", "2015-09-16", 
                  "2015-10-18", "2015-11-01", "2015-12-24", "2015-01-08", "2015-02-26", "2015-03-07", 
                  "2015-04-28", "2015-05-15", "2015-06-03", "2015-07-12", "2015-08-14", "2015-09-23", "2015-10-05", "2015-11-11", "2015-12-27", 
                  "2015-01-18", "2015-02-03", "2015-03-26", "2015-04-11", "2015-05-26", "2015-06-17", "2015-07-02", "2015-08-09", "2015-09-20", 
                  "2015-10-13", "2015-11-22", "2015-12-06", "2015-01-14", "2015-02-19", "2015-03-09", "2015-04-02", "2015-05-30", "2015-06-08", 
                  "2015-07-17", "2015-08-20", "2015-09-05", "2015-10-22", "2015-11-05", "2015-12-16", "2015-01-28", "2015-02-08", "2015-03-23", 
                  "2015-04-17", "2015-05-10", "2015-06-27", "2015-07-06", "2015-08-01", "2015-09-08", "2015-10-25", "2015-11-17", "2015-12-30", 
                  "2015-01-12", "2015-02-13", "2015-03-17", "2015-04-23", "2015-05-04", "2015-06-13", "2015-07-29", "2015-08-12", "2015-09-03", 
                  "2015-10-29", "2015-11-14", "2015-12-10", "2015-01-26", "2015-02-22", "2015-03-03", "2015-04-05", "2015-05-29", "2015-06-02", 
                  "2015-07-22", "2015-08-05", "2015-09-18", "2015-10-07", "2015-11-26", "2015-12-20", "2015-01-21", "2015-02-07", "2015-03-30", 
                  "2015-04-14", "2015-05-19", "2015-06-29", "2016-07-15", "2016-08-25", "2016-09-11", "2016-10-09", "2016-11-02", "2016-12-28", 
                  "2016-01-07", "2016-02-15", "2016-03-25", "2016-04-06", "2016-05-10", "2016-06-28", "2016-07-15", "2016-08-24", "2016-09-11", 
                  "2016-10-18", "2016-11-01", "2016-12-22", "2016-01-18", "2016-02-03", "2016-03-26", "2016-04-11", "2016-05-29", "2016-06-15", 
                  "2016-07-20", "2016-08-12", "2016-09-23", "2016-10-05", "2016-11-11", "2016-12-27", "2016-01-28", "2016-02-08", "2016-03-27", 
                  "2016-04-20", "2016-05-05", "2016-06-20", "2016-07-02", "2016-08-19", "2016-09-26", "2016-10-13", "2016-11-22", "2016-12-06", 
                  "2016-01-14", "2016-02-21", "2016-03-09", "2016-04-02", "2016-05-28", "2016-06-08", "2016-07-17", "2016-08-21", "2016-09-02", 
                  "2016-10-27", "2016-11-05", "2016-12-18", "2016-01-23", "2016-02-18", "2016-03-02", "2016-04-24", "2016-05-15", "2016-06-25", 
                  "2016-07-05", "2016-08-03", "2016-09-07", "2016-10-29", "2016-11-14", "2016-12-12", "2016-01-26", "2016-02-22", "2016-03-05", 
                  "2016-04-15", "2016-05-19", "2016-06-22", "2016-07-29", "2016-08-16", "2016-09-20", "2016-10-07", "2016-11-26", "2016-12-17", 
                  "2016-01-11", "2016-02-07", "2016-03-27", "2016-04-14", "2016-05-17", "2016-06-29", "2016-07-13", "2016-08-23", "2016-09-11", 
                  "2016-10-09", "2016-11-02", "2016-12-28", "2017-01-05", "2017-02-15", "2017-03-20", "2017-04-07", "2017-05-11", "2017-06-23", 
                  "2017-07-09", "2017-08-29", "2017-09-16", "2017-10-18", "2017-11-01", "2017-12-24", "2017-01-08", "2017-02-26", "2017-03-07", 
                  "2017-04-28", "2017-05-15", "2017-06-03", "2017-07-12", "2017-08-14", "2017-09-23", "2017-10-05", "2017-11-11", "2017-12-27", 
                  "2017-01-18", "2017-02-03", "2017-03-26", "2017-04-11", "2017-05-26", "2017-06-17", "2017-07-02", "2017-08-09", "2017-09-20", 
                  "2017-10-13", "2017-11-22", "2017-12-06", "2017-01-14", "2017-02-19", "2017-03-09", "2017-04-02", "2017-05-30", "2017-06-08", 
                  "2017-07-17", "2017-08-20", "2017-09-05", "2017-10-22", "2017-11-05", "2017-12-16", "2017-01-28", "2017-02-08", "2017-03-23", 
                  "2017-04-17", "2017-05-10", "2017-06-27", "2017-07-06", "2017-08-01", "2017-09-08", "2017-10-25", "2017-11-17", "2017-12-30", 
                  "2017-01-12", "2017-02-13", "2017-03-17", "2017-04-23", "2017-05-04", "2017-06-13", "2017-07-29", "2017-08-12", "2017-09-03", 
                  "2017-10-29", "2017-11-14", "2017-12-10", "2017-01-26", "2017-02-22", "2017-03-03", "2017-04-05", "2017-05-29", "2017-06-02", 
                  "2017-07-22", "2017-08-05", "2017-09-18", "2017-10-07", "2017-11-26", "2017-12-20", "2017-01-21", "2017-02-07", "2017-03-30", 
                  "2017-04-14", "2017-05-19", "2017-06-29", "2018-07-15", "2018-08-25", "2018-09-11", "2018-10-09", "2018-11-02", "2018-12-28", 
                  "2018-01-07", "2018-02-15", "2018-03-25", "2018-04-06", "2018-05-10", "2018-06-28", "2018-07-15", "2018-08-24", "2018-09-11", 
                  "2018-10-18", "2018-11-01", "2018-12-22", "2018-01-18", "2018-02-03", "2018-03-26", "2018-04-11", "2018-05-29", "2018-06-15", 
                  "2018-07-20", "2018-08-12", "2018-09-23", "2018-10-05", "2018-11-11", "2018-12-27", "2018-01-28", "2018-02-08", "2018-03-27", 
                  "2018-04-20", "2018-05-05", "2018-06-20", "2018-07-02", "2018-08-19", "2018-09-26", "2018-10-13", "2018-11-22", "2018-12-06", 
                  "2018-01-14", "2018-02-21", "2018-03-09", "2018-04-02", "2018-05-28", "2018-06-08", "2018-07-17", "2018-08-21", "2018-09-02", 
                  "2018-10-27", "2018-11-05", "2018-12-18", "2018-01-23", "2018-02-18", "2018-03-02", "2018-04-24", "2018-05-15", "2018-06-25", 
                  "2018-07-05", "2018-08-03", "2018-09-07", "2018-10-29", "2018-11-14", "2018-12-12", "2018-01-26", "2018-02-22", "2018-03-05", 
                  "2018-04-15", "2018-05-19", "2018-06-22", "2018-07-29", "2018-08-16", "2018-09-20", "2018-10-07", "2018-11-26", "2018-12-17", 
                  "2018-01-11", "2018-02-07", "2018-03-27", "2018-04-14", "2018-05-17", "2018-06-29", "2018-07-13", "2018-08-23", "2018-09-11",
                  "2018-10-09", "2018-11-02", "2018-12-28"]

addresses_students = []

for _ in range(450):
    street = random.choice(["Starowiejska", "Wladyslawa IV", "Morska", "Legionow", "3 Maja", "Wiejska", "Armii Krajowej",
                            "Wiczlina", "Jana z Kolna", "Akademicka", "Pucka", "Swietokrzyska", "Slowackiego", "Kosciuszki",
                            "Abrahama", "Paderewskiego", "Wzgorze Sw. Maksymiliana", "Sobotka", "Chwarznienska", "Chopina",
                            "Kaszubska", "Marynarki Polskiej", "Derdowskiego", "Powstania Styczniowego", "Hutnicza", "Kielecka",
                            "Polska", "Wzgorze Nawiedzenia", "Komuny Paryskiej"])
    number = random.randint(1, 100)
    address = f"Gdynia, {street} {number}"
    addresses_students.append(address)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "z"]

name_courses = ["Fun with Colors", "Story Time Adventures", "Creative Arts and Crafts", "Music and Movement", "Nature Explorers", 
                "Outdoor Adventures", "Little Scientists", "Exploring Shapes and Patterns", "Drama and Imagination", "Garden Explorers", 
                "Cooking Creations", "Building with Blocks", "Exploring the Universe", "Sports and Games", "Animal Adventures", 
                "Sensory Playtime", "Math Mania", "Exploring World Cultures", "Little Chefs", "Musical Melodies"]

months = ["September", "October", "November", "December", "January", "February", "March", "April", "May", "June"]

if False:
    with open('teachers_csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        
        for ID in range(1, 31):
            name = names_teacher[random.randint(0,len(names_teacher)-1)]
            surname = surnames_teacher[random.randint(0,len(surnames_teacher)-1)]
            if name[-1] != 'a' and surname[-1] == 'a':
                surname = surname[:-1] + 'i'
            date = dates_teacher[ID-1]
            gender = 'woman' if name[-1] == 'a' else 'man'
            address = addresses_teacher[ID-1]
            work = working_since[ID-1]
            contact = str(name[0]) + str(surname) + "@gmail.com"
            
            csv_writer.writerow([ID, name, surname, date, gender, address, work, contact.lower()])

if False:  
    with open('groups_csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for year in range(2018,2022):
            for ID_ in range(1, 5):
                ID = ID_ + (year - 2017) *4
                name = group_names[ID_]
                csv_writer.writerow([ID, name, year, ID])
                
if False:
    with open('students_csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for ID in range(1, 451):
            name = names_students[random.randint(0,len(names_students)-1)]
            surname = surnames_students[random.randint(0,len(surnames_students)-1)]
            if name[-1] != 'a' and surname[-1] == 'a':
                surname = surname[:-1] + 'i'
            date = dates_students[ID-1]
            gender = 'woman' if name[-1] == 'a' else 'man'
            address = addresses_students[ID-1]
            contact = str(letters[random.randint(0, len(letters)-1)]) + str(surname) + "@gmail.com"
            csv_writer.writerow([ID, name, surname, date, gender, address, contact])
            
if False:
    with open('courses_csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for ID in range(1, 21):
            name = name_courses[ID-1]
            year = int((ID-1)/5 + 1)
            teacher = ID + 10
            csv_writer.writerow([ID, name, year, teacher])
            
if True:
    with open('tests_csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for ID in range(1, 401):
            date = '2020' if ID <= 200 else '2021'
            date += str(' ') + months[(ID-1)%10]
            course = int((ID-1)/10 + 1) if ID <= 200 else int((ID-201)/10 + 1)
            csv_writer.writerow([ID, date, course])