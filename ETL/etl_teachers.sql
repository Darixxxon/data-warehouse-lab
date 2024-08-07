USE DW
GO

If (object_id('vETLDimTeachers') is not null) DROP VIEW vETLDimTeachers;
go

CREATE VIEW vETLDimTeachers
AS
SELECT DISTINCT
	[teacher_ID],
	[teacher_name],
	[teacher_surname],
	[teacher_address]
FROM [DB].dbo.[Teachers];
go


MERGE INTO DimTeachers as TT
	USING vETLDimTeachers as ST
		ON TT.t_ID = ST.teacher_ID
			WHEN Not Matched
				THEN 
					INSERT VALUES (
					ST.teacher_ID,
					ST.teacher_name,
					ST.teacher_surname,
					ST.teacher_address,
					1
					)
			WHEN Matched
			AND ST.teacher_address <> TT.teacher_address
			THEN 
				 UPDATE
				 SET TT.is_current = 0
			;

INSERT INTO DimTeachers(
	t_ID,
	teacher_name,
	teacher_surname,
	teacher_address,
	is_current)
	SELECT 
		teacher_ID,
		teacher_name,
		teacher_surname,
		teacher_address,
		1
	FROM vETLDimTeachers
	EXCEPT
	SELECT 
		t_ID,
		teacher_name,
		teacher_surname,
		teacher_address,
		1
	FROM DimTeachers;



DROP VIEW vETLDimTeachers
