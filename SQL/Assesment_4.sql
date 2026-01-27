select * from employees;
select * from department;

-- Find employees earning more than average salary.

select emp_name, emp_id, salary
from employees
where salary >(select avg(salary) from employees);

-- Find department with highest total salary.

select dept_name, sum(salary) as total_sal
from employees e
join department d
on d.dept_id = e.dept_id 
group by d.dept_name order by total_sal desc;

-- Display employee with second highest salary 

select top 2 emp_name, emp_id, salary
from employees order by salary desc ;

-- Display employees working in same department as "Nij Bhavsar".

select emp_name
from employees
where dept_id = (
    select dept_id
    from employees
    where emp_name = 'Nij Bhavsar'
)
and exists (
    select 1
    from employees
    where emp_name = 'Nij Bhavsar'
);