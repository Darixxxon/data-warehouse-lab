USE DW
go

If (object_id('vETLFPresence') is not null) DROP VIEW vETLFPresence;
go
CREATE VIEW vETLFPresence
AS
SELECT
	date_ID,
	student_ID,
	group_ID,
	teacher_ID,
	course_ID,
	Junk_presence_ID,
	class_ID
	FROM
	(
		SELECT
			date_ID = DimDate.date_ID,
			student_ID = DimStudents.student_ID,
			group_ID = DimGroups.group_ID,
			teacher_ID = tDimTeachers.teacher_ID,
			course_ID = DimCourses.course_ID,
			junk_presence_ID = DimJunkPresence.junk_presence_ID,
			class_ID = [DB].dbo.Classes.class_ID
		FROM [DB].dbo.Attendance
		JOIN DimStudents ON DimStudents.s_ID = [DB].dbo.Attendance.student_ID
		JOIN [DB].dbo.Classes ON [DB].dbo.Classes.class_ID = [DB].dbo.Attendance.class_ID
		JOIN [DB].dbo.Courses ON [DB].dbo.Courses.course_ID = [DB].dbo.Classes.course_ID
		JOIN(
			SELECT *
			FROM DimTeachers
			WHERE is_current =1
			)AS tDimTeachers 
			ON tDimTeachers.t_ID = [DB].dbo.Courses.teacher_ID
		JOIN DimGroups ON DimGroups.g_ID = [DB].dbo.Classes.group_ID
		JOIN DimDate ON DimDate.date = [DB].dbo.Attendance.attendance_date
		JOIN DimCourses ON DimCourses.c_ID = [DB].dbo.Courses.course_ID
		JOIN DimJunkPresence ON DimJunkPresence.is_present = [DB].dbo.Attendance.presence
		) AS v
go

MERGE INTO FPresence as TT
	USING vETLFPresence as ST
		ON 
			TT.date_ID = ST.date_ID
		AND TT.student_ID = ST.student_ID
		AND TT.group_ID = ST.group_ID
		AND TT.teacher_ID <> ST.teacher_ID
		AND TT.course_ID = ST.course_ID
		AND TT.junk_presence_ID = ST.junk_presence_ID
		AND TT.class_ID = ST.class_ID
			WHEN Matched
				THEN
					UPDATE
					SET TT.teacher_ID = ST.teacher_ID
;

MERGE INTO FPresence as TT
	USING vETLFPresence as ST
		ON 
			TT.date_ID = ST.date_ID
		AND TT.student_ID = ST.student_ID
		AND TT.group_ID = ST.group_ID
		AND TT.teacher_ID = ST.teacher_ID
		AND TT.course_ID = ST.course_ID
		AND TT.junk_presence_ID = ST.junk_presence_ID
		AND TT.class_ID = ST.class_ID
			WHEN Not Matched
				THEN
					INSERT
					Values (
						ST.date_ID,
						ST.student_ID,
						ST.group_ID,
						ST.teacher_ID,
						ST.course_ID,
						ST.junk_presence_ID,
						ST.class_ID
					)
;

			


DROP view vETLFPresence;
