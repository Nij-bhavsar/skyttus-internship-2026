use ecommerce;

-- Add index to improve search on orders.customer_id.

create index idx_orders_customer_id
on orders(customer_id);

-- Use EXPLAIN to analyze query.

set statistics profile on;
select * from orders where customer_id = 2;
set statistics profile off;

-- Optimize a slow join query.
select 
    c.name, 
    o.order_date, 
    o.amount
from customers c
join orders o on c.customer_id = o.customer_id
where o.order_date > '2024-01-01';

--- Explain when index should not used.

-- without using index
select * from orders where amount > 5000;

-- by using of index
select * from orders where order_id =2001; 