use company_db;

-- Create users table with:
-- Primary key, Unique email
-- Not null password
-- Add foreign key between orders and users.

create table users (
    user_id int primary key,
    email varchar(100) unique not null,
    password varchar(100) not null
);

create table orders(
order_id int,
user_id int references users(user_id),
order_date date,
total_amount decimal(10,2));

-- Create index on email column. 
create index idx_users_email on users(email);

-- Create view to display user order.

create view user_order_summary as
select 
    u.user_id,
    u.email,
    o.order_id,
    o.order_date,
    o.total_amount
from users u
join orders o
on u.user_id = o.order_id;

select * from user_order_summary;