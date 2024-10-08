import csv
import random
import time

start_time = time.time()

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

addresses = ["Gdynia Swietojanska", "Gdynia Starowiejska", "Gdynia Wladyslawa IV", "Gdynia Morska",
                     "Gdynia Legionow", "Gdynia 3 Maja", "Gdynia Wiejska", "Gdynia Armii Krajowej",
                     "Gdynia Wiczlina", "Gdynia Jana z Kolna", "Gdynia Akademicka", "Gdynia Pucka",
                     "Gdynia Swietokrzyska", "Gdynia Slowackiego", "Gdynia Kosciuszki", "Gdynia Abrahama",
                     "Gdynia Paderewskiego", "Gdynia Wzgorze Sw. Maksymiliana", "Gdynia Sobotki", "Gdynia Chwarznienska",
                     "Gdynia Chopina 66", "Gdynia Kaszubska 49", "Gdynia Marynarki Polskiej 23", "Gdynia Derdowskiego",
                     "Gdynia Powstania Styczniowego", "Gdynia Hutnicza", "Gdynia Kielecka", "Gdynia Polska",
                     "Gdynia Wzgorze Nawiedzenia", "Gdynia Komuny Paryskiej"]

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

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "z"]

name_courses = ["Fun with Colors", "Story Time Adventures", "Creative Arts and Crafts", "Music and Movement", "Nature Explorers",
                "Outdoor Adventures", "Little Scientists", "Exploring Shapes and Patterns", "Drama and Imagination", "Garden Explorers",
                "Cooking Creations", "Building with Blocks", "Exploring the Universe", "Sports and Games", "Animal Adventures",
                "Sensory Playtime", "Math Mania", "Exploring World Cultures", "Little Chefs", "Musical Melodies"]

months = ["September", "October", "November", "December",
          "January", "February", "March", "April", "May", "June"]

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

start_hour = ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00"]

end_hour = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"]

days_2020 = ["xxxx-xx-xx", "2020-09-01", "2020-09-02", "2020-09-03", "2020-09-04",
             "2020-09-07", "2020-09-08", "2020-09-09", "2020-09-10", "2020-09-11",
             "2020-09-14", "2020-09-15", "2020-09-16", "2020-09-17", "2020-09-18",
             "2020-09-21", "2020-09-22", "2020-09-23", "2020-09-24", "2020-09-25",
             "2020-09-28", "2020-09-29", "2020-09-30", "2020-10-01", "2020-10-02",
             "2020-10-05", "2020-10-06", "2020-10-07", "2020-10-08", "2020-10-09",
             "2020-10-12", "2020-10-13", "2020-10-14", "2020-10-15", "2020-10-16",
             "2020-10-19", "2020-10-20", "2020-10-21", "2020-10-22", "2020-10-23",
             "2020-10-26", "2020-10-27", "2020-10-28", "2020-10-29", "2020-10-30",
             "2020-11-02", "2020-11-03", "2020-11-04", "2020-11-05", "2020-11-06",
             "2020-11-09", "2020-11-10", "2020-11-11", "2020-11-12", "2020-11-13",
             "2020-11-16", "2020-11-17", "2020-11-18", "2020-11-19", "2020-11-20",
             "2020-11-23", "2020-11-24", "2020-11-25", "2020-11-26", "2020-11-27",
             "2020-11-30", "2020-12-01", "2020-12-02", "2020-12-03", "2020-12-04",
             "2020-12-07", "2020-12-08", "2020-12-09", "2020-12-10", "2020-12-11",
             "2020-12-14", "2020-12-15", "2020-12-16", "2020-12-17", "2020-12-18",
             "2020-12-21", "2020-12-22", "2020-12-23", "2020-12-24", "2020-12-25",
             "2020-12-28", "2020-12-29", "2020-12-30", "2020-12-31", "2021-01-01",
             "2021-01-04", "2021-01-05", "2021-01-06", "2021-01-07", "2021-01-08",
             "2021-01-11", "2021-01-12", "2021-01-13", "2021-01-14", "2021-01-15",
             "2021-01-18", "2021-01-19", "2021-01-20", "2021-01-21", "2021-01-22",
             "2021-01-25", "2021-01-26", "2021-01-27", "2021-01-28", "2021-01-29",
             "2021-02-01", "2021-02-02", "2021-02-03", "2021-02-04", "2021-02-05",
             "2021-02-08", "2021-02-09", "2021-02-10", "2021-02-11", "2021-02-12",
             "2021-02-15", "2021-02-16", "2021-02-17", "2021-02-18", "2021-02-19",
             "2021-02-22", "2021-02-23", "2021-02-24", "2021-02-25", "2021-02-26",
             "2021-03-01", "2021-03-02", "2021-03-03", "2021-03-04", "2021-03-05",
             "2021-03-08", "2021-03-09", "2021-03-10", "2021-03-11", "2021-03-12",
             "2021-03-15", "2021-03-16", "2021-03-17", "2021-03-18", "2021-03-19",
             "2021-03-22", "2021-03-23", "2021-03-24", "2021-03-25", "2021-03-26",
             "2021-03-29", "2021-03-30", "2021-03-31", "2021-04-01", "2021-04-02",
             "2021-04-05", "2021-04-06", "2021-04-07", "2021-04-08", "2021-04-09",
             "2021-04-12", "2021-04-13", "2021-04-14", "2021-04-15", "2021-04-16",
             "2021-04-19", "2021-04-20", "2021-04-21", "2021-04-22", "2021-04-23",
             "2021-04-26", "2021-04-27", "2021-04-28", "2021-04-29", "2021-04-30",
             "2021-05-03", "2021-05-04", "2021-05-05", "2021-05-06", "2021-05-07",
             "2021-05-10", "2021-05-11", "2021-05-12", "2021-05-13", "2021-05-14",
             "2021-05-17", "2021-05-18", "2021-05-19", "2021-05-20", "2021-05-21",
             "2021-05-24", "2021-05-25", "2021-05-26", "2021-05-27", "2021-05-28",
             "2021-05-31", "2021-06-01", "2021-06-02", "2021-06-03", "2021-06-04",
             "2021-06-07", "2021-06-08", "2021-06-09", "2021-06-10", "2021-06-11",
             "2021-06-14", "2021-06-15", "2021-06-16", "2021-06-17", "2021-06-18",
             "2021-06-21", "2021-06-22", "2021-06-23", "2021-06-24", "2021-06-25",
             "2021-06-28", "2021-06-29", "2021-06-30", "xxxx-xx-xx", "xxxx-xx-xx"]

days_2021 = ["xxxx-xx-xx", "xxxx-xx-xx", "2021-09-01", "2021-09-02", "2021-09-03",
             "2021-09-06", "2021-09-07", "2021-09-08", "2021-09-09", "2021-09-10",
             "2021-09-13", "2021-09-14", "2021-09-15", "2021-09-16", "2021-09-17",
             "2021-09-20", "2021-09-21", "2021-09-22", "2021-09-23", "2021-09-24",
             "2021-09-27", "2021-09-28", "2021-09-29", "2021-09-30", "2021-10-01",
             "2021-10-04", "2021-10-05", "2021-10-06", "2021-10-07", "2021-10-08",
             "2021-10-11", "2021-10-12", "2021-10-13", "2021-10-14", "2021-10-15",
             "2021-10-18", "2021-10-19", "2021-10-20", "2021-10-21", "2021-10-22",
             "2021-10-25", "2021-10-26", "2021-10-27", "2021-10-28", "2021-10-29",
             "2021-11-01", "2021-11-02", "2021-11-03", "2021-11-04", "2021-11-05",
             "2021-11-08", "2021-11-09", "2021-11-10", "2021-11-11", "2021-11-12",
             "2021-11-15", "2021-11-16", "2021-11-17", "2021-11-18", "2021-11-19",
             "2021-11-22", "2021-11-23", "2021-11-24", "2021-11-25", "2021-11-26",
             "2021-11-29", "2021-11-30", "2021-12-01", "2021-12-02", "2021-12-03",
             "2021-12-06", "2021-12-07", "2021-12-08", "2021-12-09", "2021-12-10",
             "2021-12-13", "2021-12-14", "2021-12-15", "2021-12-16", "2021-12-17",
             "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23", "2021-12-24",
             "2021-12-27", "2021-12-28", "2021-12-29", "2021-12-30", "2021-12-31",
             "2022-01-03", "2022-01-04", "2022-01-05", "2022-01-06", "2022-01-07",
             "2022-01-10", "2022-01-11", "2022-01-12", "2022-01-13", "2022-01-14",
             "2022-01-17", "2022-01-18", "2022-01-19", "2022-01-20", "2022-01-21",
             "2022-01-24", "2022-01-25", "2022-01-26", "2022-01-27", "2022-01-28",
             "2022-01-31", "2022-02-01", "2022-02-02", "2022-02-03", "2022-02-04",
             "2022-02-07", "2022-02-08", "2022-02-09", "2022-02-10", "2022-02-11",
             "2022-02-14", "2022-02-15", "2022-02-16", "2022-02-17", "2022-02-18",
             "2022-02-21", "2022-02-22", "2022-02-23", "2022-02-24", "2022-02-25",
             "2022-02-28", "2022-03-01", "2022-03-02", "2022-03-03", "2022-03-04",
             "2022-03-07", "2022-03-08", "2022-03-09", "2022-03-10", "2022-03-11",
             "2022-03-14", "2022-03-15", "2022-03-16", "2022-03-17", "2022-03-18",
             "2022-03-21", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03-25",
             "2022-03-28", "2022-03-29", "2022-03-30", "2022-03-31", "2022-04-01",
             "2022-04-04", "2022-04-05", "2022-04-06", "2022-04-07", "2022-04-08",
             "2022-04-11", "2022-04-12", "2022-04-13", "2022-04-14", "2022-04-15",
             "2022-04-18", "2022-04-19", "2022-04-20", "2022-04-21", "2022-04-22",
             "2022-04-25", "2022-04-26", "2022-04-27", "2022-04-28", "2022-04-29",
             "2022-05-02", "2022-05-03", "2022-05-04", "2022-05-05", "2022-05-06",
             "2022-05-09", "2022-05-10", "2022-05-11", "2022-05-12", "2022-05-13",
             "2022-05-16", "2022-05-17", "2022-05-18", "2022-05-19", "2022-05-20",
             "2022-05-23", "2022-05-24", "2022-05-25", "2022-05-26", "2022-05-27",
             "2022-05-30", "2022-05-31", "2022-06-01", "2022-06-02", "2022-06-03",
             "2022-06-06", "2022-06-07", "2022-06-08", "2022-06-09", "2022-06-10",
             "2022-06-13", "2022-06-14", "2022-06-15", "2022-06-16", "2022-06-17",
             "2022-06-20", "2022-06-21", "2022-06-22", "2022-06-23", "2022-06-24",
             "2022-06-27", "2022-06-28", "2022-06-29", "2022-06-30", "xxxx-xx-xx"]

if False:
    with open('teachers_2020-2021_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        #iterate through teachers
        for ID in range(1, 31):
            name = names_teacher[random.randint(0, len(names_teacher)-1)]
            surname = surnames_teacher[random.randint(
                0, len(surnames_teacher)-1)]
            if name[-1] != 'a' and surname[-1] == 'a':
                surname = surname[:-1] + 'i'
            date = dates_teacher[ID-1]
            gender = 'woman' if name[-1] == 'a' else 'man'
            address = addresses[random.randint(0,len(addresses)-1)] + ' ' + str(random.randint(1,100)) + " " + letters[random.randint(0,2)] + '/' + str(random.randint(1,10))
            work = working_since[ID-1]
            contact = str(name[0]) + str(surname) + "@gmail.com"

            csv_writer.writerow(
                [ID, name, surname, date, gender, address, work, contact.lower()])
    
    with open('teachers_2021-2022_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        #no new teachers

if False:
    with open('groups_2020-2021_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        #iterate through years
        for year in range(2017, 2021):
            #iterate through groups per year
            for ID_ in range(1, 4):
                ID = ID_ + (year - 2017) * 3
                name = group_names[ID-1]
                csv_writer.writerow([ID, name, year, ID])
    
    with open('groups_2021-2022_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        #iterate through years
        for year in range(2021, 2022):
            #iterate through groups per year
            for ID_ in range(1, 4):
                ID = ID_ + (year - 2017) * 3
                name = group_names[ID-1]
                csv_writer.writerow([ID, name, year, ID])

if False:
    with open('students_2020-2021_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        #iterate through students
        for ID in range(1, 361):
            name = names_students[random.randint(0, len(names_students)-1)]
            surname = surnames_students[random.randint(
                0, len(surnames_students)-1)]
            if name[-1] != 'a' and surname[-1] == 'a':
                surname = surname[:-1] + 'i'
            date = dates_students[ID-1]
            gender = 'woman' if name[-1] == 'a' else 'man'
            address = addresses[random.randint(0,len(addresses)-1)] + ' ' + str(random.randint(1,100)) + " " + letters[random.randint(0,2)] + '/' + str(random.randint(1,10))
            contact = str(letters[random.randint(
                0, len(letters)-1)]) + str(surname) + "@gmail.com"
            group = int((ID-1)/30)+1
            csv_writer.writerow(
                [ID, name, surname, date, gender, address, contact.lower(), group])
            
    with open('students_2021-2022_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        #iterate through students
        for ID in range(361, 451):
            name = names_students[random.randint(0, len(names_students)-1)]
            surname = surnames_students[random.randint(
                0, len(surnames_students)-1)]
            if name[-1] != 'a' and surname[-1] == 'a':
                surname = surname[:-1] + 'i'
            date = dates_students[ID-1]
            gender = 'woman' if name[-1] == 'a' else 'man'
            address = addresses[random.randint(0,len(addresses)-1)] + ' ' + str(random.randint(1,100)) + " " + letters[random.randint(0,2)] + '/' + str(random.randint(1,10))
            contact = str(letters[random.randint(
                0, len(letters)-1)]) + str(surname) + "@gmail.com"
            group = int((ID-1)/30)+1
            csv_writer.writerow(
                [ID, name, surname, date, gender, address, contact.lower(), group])

if False:
    with open('courses_2020-2021_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        #iterate through courses
        for ID in range(1, 21):
            name = name_courses[ID-1]
            year = int((ID-1)/5 + 1)
            teacher = ID + 10
            csv_writer.writerow([ID, name, year, teacher])
        
    with open('courses_2021-2022_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        #no new courses

if False:
    with open('tests_2020-2021_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        #iterate through testes, 20 courses times 10 months
        for ID in range(1, 201):
            if (ID-1) % 10 <= 3:
                date = '2020'
            else:
                date = '2021'
            date += str(' ') + months[(ID-1) % 10]
            course = int((ID-1)/10 + 1)
            csv_writer.writerow([ID, date, course])
            
    with open('tests_2021-2022_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        #iterate through testes, 20 courses times 10 months
        for ID in range(201, 401):
            if (ID-1) % 10 > 3:
                date = '2022'
            else:
                date = '2021'
            date += str(' ') + months[(ID-1) % 10]
            course = int((ID-201)/10 + 1)
            csv_writer.writerow([ID, date, course])

if False:
    with open('classes_2020-2021_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        year = "2020/2021"
        #iterate through groups in one year
        for gr_ID in range(1, 13):
            #iterate through days in week
            for day in range(0, 5):
                #iterate through hours in one day
                for h in range(0, 6):
                    ID = ((gr_ID-1)*30) + day*6 + h + 1
                    start = start_hour[h]
                    end = end_hour[h]
                    # co_ID = (((gr_ID-1%3)+1 + int(h/3)) + int((gr_ID-1)/3)*3 + day*2 - 1)%5 +1 + int((gr_ID-1)/3)*4
                    co_ID = 21 - (((gr_ID-1) % 3+1 + int(h/3) +
                                  day*2 - 1) % 5 + 1 + int((gr_ID-1)/3)*5)
                    day_w = week[day]
                    csv_writer.writerow([ID, day_w, start, end, year, gr_ID, co_ID])
                    
    with open('classes_2021-2022_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        year =  "2021/2022"
        #iterate through groups in one year
        for gr_ID in range(1, 13):
            #iterate through days in week
            for day in range(0, 5):
                #iterate through hours in one day
                for h in range(0, 6):
                    ID = ((gr_ID-1)*30) + day*6 + h + 1
                    start = start_hour[h]
                    end = end_hour[h]
                    co_ID = 21 - (((gr_ID-1) % 3+1 + int(h/3) +
                                  day*2 - 1) % 5 + 1 + int((gr_ID-1)/3)*5)
                    day_w = week[day]
                    csv_writer.writerow([ID+360, day_w, start, end, year, gr_ID + 3, co_ID])

if False:
    with open('attendance_2020-2021_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        ID = 0
        #iterate through students
        for s_ID in range(1, 361):
            gr_ID = int((s_ID-1)/30)+1
            #iterate through days in year
            for days in range(0, len(days_2020)):
                if days == "xxxx-xx-xx":
                    continue
                #iterate through classes
                for cl_ID in range((gr_ID-1)*30+1, (gr_ID-1)*30+1+30):
                    if days % 5 == int((cl_ID-1) % 30/6):
                        ID += 1
                        if days_2020[days][5:7] == '09':
                            prob = 80
                        elif days_2020[days][5:7] == '10':
                            prob = 81
                        elif days_2020[days][5:7] == '11':
                            prob = 83
                        elif days_2020[days][5:7] == '12':
                            prob = 84
                        elif days_2020[days][5:7] == '01':
                            prob = 85
                        elif days_2020[days][5:7] == '02':
                            prob = 85
                        elif days_2020[days][5:7] == '03':
                            prob = 86
                        elif days_2020[days][5:7] == '04':
                            prob = 87
                        elif days_2020[days][5:7] == '05':
                            prob = 87
                        elif days_2020[days][5:7] == '06':
                            prob = 87
                        csv_writer.writerow([ID, True if random.randint(1, 100) <= prob else False, days_2020[days], s_ID, cl_ID])
                        
    with open('attendance_2021-2022_csv.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        #iterate through students
        for s_ID in range(91, 451):
            gr_ID = int((s_ID-1)/30)+1
            #iterate through days in year
            for days in range(0, len(days_2021)):
                if days == "xxxx-xx-xx":
                    continue
                #iterate through classes
                for cl_ID in range((gr_ID-1)*30+1 +270, (gr_ID-1)*30+1+30+270):
                    if days % 5 == int((cl_ID-1) % 30/6):
                        ID += 1
                        if days_2020[days][5:7] == '09':
                            prob = 87
                        elif days_2020[days][5:7] == '10':
                            prob = 87
                        elif days_2020[days][5:7] == '11':
                            prob = 88
                        elif days_2020[days][5:7] == '12':
                            prob = 88
                        elif days_2020[days][5:7] == '01':
                            prob = 89
                        elif days_2020[days][5:7] == '02':
                            prob = 90
                        elif days_2020[days][5:7] == '03':
                            prob = 90
                        elif days_2020[days][5:7] == '04':
                            prob = 91
                        elif days_2020[days][5:7] == '05':
                            prob = 92
                        elif days_2020[days][5:7] == '06':
                            prob = 92
                        csv_writer.writerow([ID, True if random.randint(1, 100) <= prob else False, days_2021[days], s_ID, cl_ID])
                        
if False:
    f = open('updates_teachers.txt', 'w')
    for ID in range(1, 31, 4):
        print("UPDATE Teachers SET teacher_address = '" + addresses[random.randint(0,len(addresses)-1)] +
              ' ' + str(random.randint(1,100)) + " " + letters[random.randint(0,2)] + '/' + 
              str(random.randint(1,10)) + "' WHERE teacher_ID = " + str(ID), file = f)
    f.close()
    
if False:
    f = open('updates_students.txt', 'w')
    for ID in range(1, 361, 15):
        print("UPDATE Students SET student_address = '" + addresses[random.randint(0,len(addresses)-1)] +
              ' ' + str(random.randint(1,100)) + " " + letters[random.randint(0,2)] + '/' + 
              str(random.randint(1,10)) + "' WHERE student_ID = " + str(ID), file = f)
    f.close()