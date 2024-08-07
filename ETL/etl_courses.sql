USE DW
GO

If (object_id('vETLDimCourses') is not null) DROP VIEW vETLDimCourses;
go
CREATE VIEW vETLDimCourses
AS
SELECT DISTINCT
	[course_ID],
	[name_of_course],
	CASE
		WHEN [course_year] = 1 THEN 'first year'
		WHEN [course_year] = 2 THEN 'second year'
		WHEN [course_year] = 3 THEN 'third year'
		WHEN [course_year] = 4 THEN 'fourth year'
	END AS [course_year]
FROM [DB].dbo.[Courses]
go

MERGE INTO DimCourses as TT
	USING vETLDimCourses as ST
		ON TT.c_ID = ST.course_ID
			WHEN Not Matched
				THEN 
					INSERT VALUES (
					ST.course_ID,
					ST.name_of_course,
					ST.course_year
					)
			;

DROP VIEW vETLDimCourses;