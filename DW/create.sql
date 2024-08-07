use DW

CREATE TABLE DimTeachers
(
    teacher_ID INT IDENTITY(1,1) PRIMARY KEY,
    t_ID INT NOT NULL,
    teacher_name VARCHAR(20) NOT NULL,
    teacher_surname VARCHAR(20) NOT NULL,
    teacher_address VARCHAR(50) NOT NULL,
    is_current BIT NOT NULL
);

CREATE TABLE DimGroups
(
    group_ID INT IDENTITY(1,1) PRIMARY KEY,
    g_ID INT NOT NULL,
    group_name VARCHAR(30) NOT NULL,
	starting_year VARCHAR(4) NOT NULL,
);

CREATE TABLE DimStudents
(
    student_ID INT IDENTITY(1,1) PRIMARY KEY,
    s_ID INT NOT NULL,
    student_name VARCHAR(20) NOT NULL,
    student_surname VARCHAR(20) NOT NULL
);

CREATE TABLE DimCourses
(
    course_ID INT IDENTITY(1,1) PRIMARY KEY,
    c_ID INT NOT NULL,
    name_of_course VARCHAR(30) NOT NULL,
    course_year VARCHAR(15) NOT NULL
);

CREATE TABLE DimDate
(
    date_ID INT IDENTITY(1,1) PRIMARY KEY,
    date date NOT NULL,
    year VARCHAR(4) NOT NULL,
    month VARCHAR(10) NOT NULL,
    month_no INT
);

CREATE TABLE DimJunkPresence
(
    junk_presence_ID INT IDENTITY(1,1) PRIMARY KEY,
    is_present VARCHAR(8)
);

CREATE TABLE FPresence
(
    date_ID INT FOREIGN KEY REFERENCES DimDate(date_ID),
    student_ID INT FOREIGN KEY REFERENCES DimStudents(student_ID),
    group_ID INT FOREIGN KEY REFERENCES DimGroups(group_ID),
    teacher_ID INT FOREIGN KEY REFERENCES DimTeachers(teacher_ID),
    course_ID INT FOREIGN KEY REFERENCES DimCourses(course_ID),
    junk_presence_ID INT FOREIGN KEY REFERENCES DimJunkPresence(junk_presence_ID),
    class_ID INT 
    PRIMARY KEY(date_ID, student_ID, group_ID, teacher_ID, course_ID, junk_presence_ID, class_ID)
);

CREATE TABLE FGrading
(
    test_ID INT,
    student_ID INT FOREIGN KEY REFERENCES DimStudents(student_ID),
    course_ID INT FOREIGN KEY REFERENCES DimCourses(course_ID),
    teacher_ID INT FOREIGN KEY REFERENCES DimTeachers(teacher_ID),
    date_ID INT FOREIGN KEY REFERENCES DimDate(date_ID),
    group_ID INT FOREIGN KEY REFERENCES DimGroups(group_ID),
    percentage_of_points FLOAT,
    time_percentage_used FLOAT,
    grade INT,
    PRIMARY KEY(test_ID, student_ID, course_ID, teacher_ID, date_ID, group_ID)
)