-------------------------------------------------------------------------
--Q1---------------------------------------------------------------------
/*
Given a table events with following strucutre: 
create table events 
    (sensor_id integer not null, 
    event_type integer not null, 
    value float not null, 
    time timestamp not null);

Write an sql query that returns a set of all sensors (sensor_id) with 
the number of different event types(event_type) registered by each of them, ordered by sensor_id (in ascending order). 
expected output should be two columns sensor_id and types
*/
SELECT sensor_id, COUNT(DISTINCT event_type) AS types
-- columns as needed 
From events
Group by sensor_id
-- need the order
Order by sensor_id ASC;

-------------------------------------------------------------------------
--Q2---------------------------------------------------------------------
/* An automatic judging system checks a solution for the task on multiple test cases.The outcome of a test case is binary: either the solution succeeds or fails. 
But not all test cases are equally important. each test case assigned to a group and every test case in group is worth the same number of points.
You have receveid a raw report with the results of the automatic testing. the report consists of two tables, 
test_groups and test_cases with following strcuture: 
create table test_groups (
            name varchar(40) not null, 
            test_vallue integer not null, 
            unique(name));

and create table test_cases (
            id integer not null, 
            group_name varchar(40) not null, 
            status varchar(5) not null, unique(id) );

Each row of the table test_groups contains information about a single group of tests: unique name(name) and thhe value of each test in the group(test_value).
Each row of the table test_cases contains information about a single test case:unique id(id), the name of the group to which it belongs(group_name) and status(status)
Status contains either one of two possible words: OK or ERROR.

Write an SQL query that summarises each group of tests. 
The table of results should contian four columns: 
name(name of the group), 
all_test_cases(number of tests in group)
passes_test_cases(number of test cases with status OK),
and total_value(total value of passed tests in this group).

Rows should be ordered by decreasing total_value. In the case of a tie, rows should be sorted lexigraphically by name.

*/
SELECT 
g.name 
-- to account for corner cases use coalesce
,coalesce(count(c.id),0) as all_test_cases
,coalesce(sum(CASE when c.status ='OK' then 1 else 0 end),0) as passed_test_cases
,coalesce(sum(CASE when c.status ='OK' then g.test_value else 0 end),0) as total_value
-- brackets
from
test_groups g
left join 
-- note not join 
test_cases c
on g.name=c.group_name
group by
g.name
,g.test_value
order by
--note order
total_value desc
,g.name asc;