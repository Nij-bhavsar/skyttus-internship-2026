create database ecommerce;
use ecommerce;

create table customers(
	customer_id int primary key, 
	name varchar(100) not null, 
	city varchar(50)
	);

create table orders(
	order_id int primary key, 
	customer_id int, 
	order_date date, 
	amount decimal(10,2),
	foreign key(customer_id) references customers(customer_id)
	);

create table products(
	product_id int primary key, 
	product_name varchar(100) not null, 
	price decimal(10,2) not null
	);

create table order_items(
	order_id int, 
	product_id int, 
	quantity int not null,
	primary key (order_id, product_id),
    foreign key (order_id) references orders(order_id),
    foreign key (product_id) references products(product_id)
);

insert into customers (customer_id, name, city) values
(1, 'neni joshi', 'vadodara'),
(2, 'kundra mehta', 'mumbai'),
(3, 'balwinder singh', 'delhi'),
(4, 'narendra modi', 'ahmedabad'),
(5, 'mansi patel', 'surat');

insert into products (product_id, product_name, price) values
(101, 'phone', 155000.00),
(102, 'laptop', 76500.00),
(103, 'bluetooth earbuds', 2500.00),
(104, 'smart watch', 11050.00),
(105, 'keyboard', 5500.00);

insert into orders (order_id, customer_id, order_date, amount) values
(2001, 2, '2024-01-08', 3200.00),
(2002, 5, '2024-01-22', 48000.00),
(2003, 1, '2024-02-05', 15000.00),
(2004, 3, '2024-02-27', 9200.00),
(2005, 4, '2024-03-12', 61000.00),
(2006, 2, '2024-03-25', 7800.00);

insert into order_items (order_id, product_id, quantity) values
(2001, 101, 1),
(2001, 105, 2),

(2002, 102, 1),

(2003, 101, 1),
(2003, 103, 1),

(2004, 104, 1),
(2004, 105, 1),

(2005, 102, 1),
(2005, 104, 2),

(2006, 103, 1),
(2006, 105, 1);

select * from customers;
select * from products;
select * from orders;
select * from order_items;
-- Total orders per customer.

select 
    c.customer_id,
    c.name,
    count(o.order_id) as total_orders
from customers c
left join orders o
on c.customer_id = o.customer_id
group by c.customer_id, c.name;

--Customers who never placed an order.
select
    c.customer_id,
    c.name
from customers c
left join orders o
on c.customer_id = o.customer_id
where o.order_id is null;

-- Highest selling product.
select top 1
    p.product_id,
    p.product_name,
    sum(oi.quantity) as total_quantity_sold
from products p
join order_items oi
on p.product_id = oi.product_id
group by p.product_id, p.product_name
order by total_quantity_sold desc;

-- Monthly sales report.

select
    month(order_date) as month,
    year(order_date) as year,
    sum(amount) as total_sales
from orders
group by year(order_date), month(order_date)
order by year, month;

--Customers with total purchase > ?50,000.

select
    c.customer_id,
    c.name,
    sum(o.amount) as total_purchase
from customers c
join orders o
on c.customer_id = o.customer_id
group by c.customer_id, c.name
having sum(o.amount) > 50000;

-- Top 3 cities by revenue.
select top 3
    c.city,
    sum(o.amount) as total_revenue
from customers c
join orders o on c.customer_id = o.customer_id
group by c.city
order by total_revenue desc;