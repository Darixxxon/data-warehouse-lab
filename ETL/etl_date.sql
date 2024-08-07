use DW
go


Declare @StartDate date; 
Declare @EndDate date;

SELECT @StartDate = '2020-09-01', @EndDate = '2022-06-30';

Declare @DateInProcess datetime = @StartDate;

While @DateInProcess <= @EndDate
Begin

Insert Into DimDate
	( 
	[date], 
	[year],
	[month], 
	[month_no]
	)
Values ( 
	@DateInProcess, 
	Cast( Year(@DateInProcess) as varchar(4)), 
	Cast( DATENAME(month, @DateInProcess) as varchar(10)), 
	Cast( Month(@DateInProcess) as int)
);  

Set @DateInProcess = DateAdd(d, 1, @DateInProcess);
End
go