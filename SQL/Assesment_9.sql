use company_db;

-- create the table
create table employee (
    employee_id int primary key,
    name varchar(100) not null,
    salary decimal(10,2),
    hire_date date
);

-- insert sample data
insert into employee (employee_id, name, salary, hire_date) values
(101, 'raj sharma', 75000.00, '2023-05-15'),
(102, 'simran kaur', 62000.00, '2024-01-10'),
(103, 'amit verma', 85000.00, '2025-08-20'),
(104, 'sneha gupta', 55000.00, '2025-11-01'),
(105, 'vijay singh', 95000.00, '2026-01-05');

select * from employee;

create table potential_customers (
    customer_id int primary key,
    name varchar(100),
    city varchar(50)
);

insert into potential_customers (customer_id, name, city) values
(2, 'kundra mehta', 'mumbai'), 
(4, 'narendra modi', 'ahmedabad'), 
(10, 'rahul dravid', 'bangalore'), 
(11, 'sachin tendulkar', 'mumbai');

--Write query to find Nth highest salary.
select distinct salary
from employee
order by salary desc; 

--Find Records Common in Two Tables

select name 
from employee
where name in (select name from potential_customers);

-- Find Employees Hired in the Last 6 Months.

select * from employee 
where hire_date >= dateadd(month, -6, '2026-01-30');

-- Find continuous duplicate values.

insert into potential_customers values (23, 'sachin tendulkar', 'hydrabad')

select customer_id, name 
from ( select customer_id, name, lag(name) 
over (order by name) as prev_name from potential_customers ) 
sub where name = prev_name;