create database company_db;

use company_db;

create table employees
( emp_id INT, emp_name VARCHAR(50), dept_id INT, salary INT );

create table department
(dept_id INT, dept_name VARCHAR(50));

insert into employees values
(1011, 'Nij Bhavsar', 7, 31000),
(1109, 'Jeet Bhavsar', 9, 25000),
(1031, 'Sanjay Patel', 17, 30000),
(1517, 'Meet Patel', 11, 35000),
(1414, 'Het Patel', 5, 33000),
(1010, 'Drish Bhanderi', 1, 31500);

insert into department (dept_id, dept_name) values
(1, 'HR'),
(5, 'Finance'),
(7, 'IT'),
(9, 'Marketing'),
(11, 'Operations'),
(17, 'Sales');

select * from department;
select * from employees ;

-- Display employee name with department name 

SELECT e.emp_name, d.dept_name
FROM employees e
JOIN department d
ON e.dept_id = d.dept_id;

update employees
set salary = 60000
where emp_id = 1011; 

-- Display employees earning more than 50,000 
select emp_name, salary as highest_sal from employees
where salary > 50000;

-- Display department-wise total salary
select d.dept_name, sum(salary) as total_sal
from employees e
join department d 
on d.dept_id = d.dept_id
group by dept_name;

-- Display departments with more than 2 employees

select d.dept_name, count(e.emp_id) as employees_count
from employees e
join department d
on e.dept_id = d.dept_id
group by d.dept_name
having count(e.emp_id) > 2;

-- Display employees without a department.

select emp_name, emp_id from employees e
left join department d
on d.dept_id = e.dept_id 
where d.dept_id is null;