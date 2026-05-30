create table Customers(
	Customer_ID int ,
    Customer_name varchar(100),
    City varchar(50)
);

insert into Customers
values
(1,'Rasiga','Chennai'),
(2,'Priya','Bangalore'),
(3,'Harish','Hyderabad');

set  SQL_SAFE_UPDATES=0;

update Customers set City= 'Kerala'
where Customer_ID =3;

delete from Customers
where City='Bangalore';

set  SQL_SAFE_UPDATES=1;

select * from Customers;

-- create table Products(
-- 	product_id int primary key,
--     product_name varchar(100),
--     category varchar(50),
--     price decimal(10,2),
--     stock_quantity int,
--     supplier_city varchar(50)
-- );

-- insert into Products values
-- (1,'Laptop','Electronics',50000,20,'Bangalore'),
-- (2,'Smart Watch','Gadgets',2000,50,'Chennai');

-- update Products set supplier_city='Delhi'
-- where product_id=2;

-- delete from Products
-- where supplier_city='Delhi';

-- select * from Products;

-- drop table Products;


