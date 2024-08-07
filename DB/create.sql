USE DB

CREATE TABLE Teachers
(
    teacher_ID INT PRIMARY KEY,
    teacher_name VARCHAR(20) NOT NULL,
    teacher_surname VARCHAR(20) NOT NULL,
    teacher_date_of_birth DATE NOT NULL,
    teacher_gender VARCHAR(10) NOT NULL,
    teacher_address VARCHAR(50) NOT NULL,
    working_since DATE NOT NULL,
    teacher_contact VARCHAR(30) NOT NULL
);

CREATE TABLE Groups
(
    group_ID INT PRIMARY KEY,
    group_name VARCHAR(30) NOT NULL,
    starting_year INT NOT NULL,
    supervising_teacher_ID INT FOREIGN KEY REFERENCES Teachers(teacher_ID)
);

CREATE TABLE Students
(
    student_ID INT PRIMARY KEY,
    student_name VARCHAR(20) NOT NULL,
    student_surname VARCHAR(20) NOT NULL,
    student_date_of_birth DATE NOT NULL,
    student_gender VARCHAR(10) NOT NULL,
    student_address VARCHAR(50) NOT NULL,
    parents_contact VARCHAR(30) NOT NULL,
    group_ID INT FOREIGN KEY REFERENCES Groups(group_ID)
);

CREATE TABLE Courses
(
    course_ID INT PRIMARY KEY,
    name_of_course VARCHAR(30) NOT NULL,
    course_year INT NOT NULL,
    teacher_ID INT FOREIGN KEY REFERENCES Teachers(teacher_ID)
);

CREATE TABLE Tests
(
    test_ID INT PRIMARY KEY,
    date_of_test VARCHAR(15) NOT NULL,
    course_ID INT FOREIGN KEY REFERENCES Courses(course_ID)
);

CREATE TABLE Classes
(
    class_ID INT PRIMARY KEY,
    day_of_week VARCHAR(10) NOT NULL,
    start_hour TIME NOT NULL,
    end_hour TIME NOT NULL,
    year_of_classes VARCHAR(9) NOT NULL,
    group_ID INT FOREIGN KEY REFERENCES Groups(group_ID),
    course_ID INT FOREIGN KEY REFERENCES Courses(course_ID)
);

CREATE TABLE Attendance
(
    attendance_ID INT PRIMARY KEY,
    presence VARCHAR(5) NOT NULL,
    attendance_date DATE NOT NULL,
    student_ID INT FOREIGN KEY REFERENCES Students(student_ID),
    class_ID INT FOREIGN KEY REFERENCES Classes(class_ID),
    UNIQUE(attendance_date, student_ID, class_ID)
);