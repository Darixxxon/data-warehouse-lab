USE DW
go

If (object_id('dbo.GradesTemp') is not null) DROP TABLE dbo.GradesTemp;
CREATE TABLE dbo.GradesTemp(grade_ID INT, student_ID INT, test_ID INT, grade INT, percentage INT, writing_time INT, attempt_num INT);
go

BULK INSERT dbo.GradesTemp
    FROM 'C:\pollitechnika\semestr 4\Data warehouses\Sources\grades.csv'
    WITH
    (
    FIRSTROW = 1,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK
    )
IF (object_id('vETLFGrading') is not null) DROP VIEW vETLFGrading;
go
CREATE VIEW vETLFGrading
AS
SELECT
	test_ID,
	student_ID,
	course_ID,
	teacher_ID,
	date_ID,
	group_ID,
	percentage_of_points,
	time_percentage_used,
	grade
	FROM
	(
		SELECT 
			test_ID = tGradesTemp.test_ID,
			student_ID = DimStudents.student_ID,
			course_ID = DimCourses.course_ID,
			teacher_ID = tDimTeachers.teacher_ID,
			date_ID = DimDate.date_ID,
			group_ID = DimGroups.group_ID,
			percentage_of_points = CAST(tGradesTemp.percentage AS FLOAT) / 100,
			time_percentage_used = CAST(tGradesTemp.writing_time AS FLOAT) / 100,
			grade = tGradesTemp.grade
		FROM
		(
			SELECT
				*,
				CASE
					WHEN SUBSTRING([DB].dbo.Tests.date_of_test, 6, LEN([DB].dbo.Tests.date_of_test) - 5) = 'September' THEN LEFT([DB].dbo.Tests.date_of_test, 4)+'-09-30'
					WHEN SUBSTRING([DB].dbo.Tests.date_of_test, 6, LEN([DB].dbo.Tests.date_of_test) - 5) = 'October' THEN LEFT([DB].dbo.Tests.date_of_test, 4)+'-10-31'
					WHEN SUBSTRING([DB].dbo.Tests.date_of_test, 6, LEN([DB].dbo.Tests.date_of_test) - 5) = 'November' THEN LEFT([DB].dbo.Tests.date_of_test, 4)+'-11-30'
					WHEN SUBSTRING([DB].dbo.Tests.date_of_test, 6, LEN([DB].dbo.Tests.date_of_test) - 5) = 'December' THEN LEFT([DB].dbo.Tests.date_of_test, 4)+'-12-31'
					WHEN SUBSTRING([DB].dbo.Tests.date_of_test, 6, LEN([DB].dbo.Tests.date_of_test) - 5) = 'January' THEN LEFT([DB].dbo.Tests.date_of_test, 4)+'-01-31'
					WHEN SUBSTRING([DB].dbo.Tests.date_of_test, 6, LEN([DB].dbo.Tests.date_of_test) - 5) = 'February' THEN LEFT([DB].dbo.Tests.date_of_test, 4)+'-02-28'
					WHEN SUBSTRING([DB].dbo.Tests.date_of_test, 6, LEN([DB].dbo.Tests.date_of_test) - 5) = 'March' THEN LEFT([DB].dbo.Tests.date_of_test, 4)+'-03-31'
					WHEN SUBSTRING([DB].dbo.Tests.date_of_test, 6, LEN([DB].dbo.Tests.date_of_test) - 5) = 'April' THEN LEFT([DB].dbo.Tests.date_of_test, 4)+'-04-30'
					WHEN SUBSTRING([DB].dbo.Tests.date_of_test, 6, LEN([DB].dbo.Tests.date_of_test) - 5) = 'May' THEN LEFT([DB].dbo.Tests.date_of_test, 4)+'-05-31'
					WHEN SUBSTRING([DB].dbo.Tests.date_of_test, 6, LEN([DB].dbo.Tests.date_of_test) - 5) = 'June' THEN LEFT([DB].dbo.Tests.date_of_test, 4)+'-06-30'
				END AS tdate
			FROM [DB].dbo.Tests
		) AS t_tests
		JOIN(
			SELECT *
			FROM GradesTemp 
			WHERE GradesTemp.grade_ID NOT IN 
			(
				SELECT grade_ID
				FROM GradesTemp
				WHERE attempt_num = 2
			)
			) AS tGradesTemp
			ON tGradesTemp.test_ID = t_tests.test_ID
		JOIN DimStudents ON DimStudents.s_ID = tGradesTemp.student_ID
		JOIN [DB].dbo.Students ON [DB].dbo.Students.student_ID = tGradesTemp.student_ID
		JOIN [DB].dbo.Courses ON [DB].dbo.Courses.course_ID = t_tests.course_ID
		JOIN(
			SELECT *
			FROM DimTeachers
			WHERE is_current =1
			)AS tDimTeachers
			ON tDimTeachers.t_ID = [DB].dbo.Courses.teacher_ID
		JOIN DimDate ON DimDate.date = t_tests.tdate
		JOIN DimGroups ON DimGroups.g_ID = [DB].dbo.Students.group_ID
		JOIN DimCourses ON DimCourses.c_ID = t_tests.course_ID
		) AS v
go

MERGE INTO FGrading as TT
	USING vETLFGrading as ST
		ON
			TT.test_ID = ST.test_ID
		AND TT.student_ID = ST.student_ID
		AND TT.course_ID = ST.course_ID
		AND TT.teacher_ID <> ST.teacher_ID
		AND TT.date_ID = ST.date_ID
		AND TT.group_ID = ST.group_ID
			WHEN Matched
				THEN
					UPDATE
					SET TT.teacher_ID = ST.teacher_ID
	;

MERGE INTO FGrading as TT
	USING vETLFGrading as ST
		ON
			TT.test_ID = ST.test_ID
		AND TT.student_ID = ST.student_ID
		AND TT.course_ID = ST.course_ID
		AND TT.teacher_ID = ST.teacher_ID
		AND TT.date_ID = ST.date_ID
		AND TT.group_ID = ST.group_ID
			WHEN Not Matched
				THEN
					INSERT
					Values (
						ST.test_ID,
						ST.student_ID,
						ST.course_ID,
						ST.teacher_ID,
						ST.date_ID,
						ST.group_ID,
						ST.percentage_of_points,
						ST.time_percentage_used,
						ST.grade
					)
;


DROP TABLE dbo.GradesTemp
DROP VIEW vETLFGrading
