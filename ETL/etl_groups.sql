USE DW
GO

If (object_id('vETLDimGroups') is not null) DROP VIEW vETLDimGroups;
go
CREATE VIEW vETLDimGroups
AS
SELECT DISTINCT
	[group_ID],
	[group_name],
	[starting_year]
FROM [DB].dbo.[Groups]
go

MERGE INTO DimGroups as TT
	USING vETLDimGroups as ST
		ON TT.g_ID = ST.group_ID
			WHEN Not Matched
				THEN 
					INSERT VALUES (
					ST.group_ID,
					ST.group_name,
					ST.starting_year
					)
			;

DROP VIEW vETLDimGroups;