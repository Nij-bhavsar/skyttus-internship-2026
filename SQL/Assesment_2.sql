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
(6, 'Om', 'CE', 2026, 95),
(7, 'Dixit', 'ME', 2026, 89),
(8, 'Zaki', 'CSE', 2025, 18),
(9, 'Aryan', 'IT', 2026, 99),
(10, 'Krish', 'IT', 2026, 95);

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

-- count total numbers of student
select count(name) as total_students from student

-- find average marks of students
select AVG(mark) as Avg_marks from student

-- Find highest and lowest marks 
select MAX(mark) as Highest_marks,
MIN(mark) as Lowest_marks from student;

-- Find department-wise average marks
select department, AVG(mark) as Departmentwise_avg from student 
Group by department;

-- Display departments where average marks > 70
select department, AVG(mark) as Avg_marks 
from student
Group by department 
Having AVG(mark) > 70;
