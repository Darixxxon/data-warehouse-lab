USE DW
GO
If (object_id('vETLDimStudents') is not null) DROP VIEW vETLDimStudents;

go
CREATE VIEW vETLDimStudents
AS
SELECT DISTINCT
	[student_ID],
	[student_name],
	[student_surname]
FROM [DB].dbo.Students
go

MERGE INTO DimStudents as TT
	USING vETLDimStudents as ST
		ON TT.s_ID = ST.student_ID
			WHEN Not Matched
				THEN
					INSERT
					Values (
					ST.student_ID,
					ST.student_name,
					ST.student_surname
					)
			WHEN Not Matched By Source
			Then
				DELETE
;

Drop View vETLDimStudents;
