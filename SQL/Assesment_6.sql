use company_db;

create table accounts(
	account_id int primary key,
	account_holder varchar(100),
	balance decimal(10,2)
	);

-- Insert record into accounts
insert into accounts values
(1, 'Jitendra', 50000.00),
(2, 'Narendra', 30000.00);

select * from accounts;

-- Start a transaction
begin TRANSACTION;

-- Demonstrate transfer of money using transaction.
update accounts
set balance = balance - 1000
where account_id = 1;

update accounts
set balance = balance + 1000
where account_id = 2;

select * from accounts;

-- Rollback changes 
rollback;

-- Commit valid transactions
commit;