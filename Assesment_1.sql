create database Student;

use Student;

create table student(student_id int, name varchar(50), department varchar(100), 
year int, mark int);
insert into student values
(1, 'Nij Bhavsar', 'CSE', 2026, 95),
(2, 'Jil', 'ME', 2026, 89),
(3, 'Meet', 'IT', 2025, 78),
(4, 'Sanjay', 'IT', 2026, 88),
(5, 'Drish', 'IT', 2026, 95);

-- To Display all students records
select * from student;

-- Display only name and department
select name, department from student;

-- Find student with marks greater than 75
select * from student
where mark > 75

-- Display students from cse department
select * from student
where department = 'CSE'

-- Sort students by marks(Descending)
select * from student
order by mark desc

-- Display top 3 scorer
select top 3 * from student
