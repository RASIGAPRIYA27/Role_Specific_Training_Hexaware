-- create database 
CREATE DATABASE retail_capstone_db;
USE retail_capstone_db;

-- customers table
CREATE TABLE customers
(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(100),
city VARCHAR(50),
state VARCHAR(50),
gender VARCHAR(10),
membership_type VARCHAR(30)
);

-- products table
CREATE TABLE products
(
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2)
);

-- orders table
create table orders (
    order_id int primary key,
    customer_id int,
    order_date date,
    order_status varchar(30),
    foreign key (customer_id) references customers(customer_id)
);

-- order_items table
create table order_items (
    item_id int primary key,
    order_id int,
    product_id int,
    quantity int,
    foreign key (order_id) references orders(order_id),
    foreign key (product_id) references products(product_id)
);

-- payments table
create table payments (
    payment_id int primary key,
    order_id int,
    payment_mode varchar(30),
    payment_status varchar(30),
    amount decimal(10,2),
    foreign key (order_id) references orders(order_id)
);

-- deliveries table
CREATE TABLE deliveries
(
delivery_id INT PRIMARY KEY,
order_id INT,
delivery_partner VARCHAR(50),
delivery_status VARCHAR(30),
delivery_city VARCHAR(50),
foreign key (order_id) references orders(order_id)
);

insert into customers values
(1, 'Aarav Sharma', 'Hyderabad', 'Telangana', 'Male', 'Gold'),
(2, 'Diya Reddy', 'Chennai', 'Tamil Nadu', 'Female', 'Silver'),
(3, 'Vivaan Patel', 'Mumbai', 'Maharashtra', 'Male', 'Gold'),
(4, 'Ananya Singh', 'Bangalore', 'Karnataka', 'Female', 'Platinum'),
(5, 'Aditya Verma', 'Hyderabad', 'Telangana', 'Male', 'Silver'),
(6, 'Meera Nair', 'Kochi', 'Kerala', 'Female', 'Gold'),
(7, 'Krishna Iyer', 'Chennai', 'Tamil Nadu', 'Male', 'Bronze'),
(8, 'Sneha Kapoor', 'Delhi', 'Delhi', 'Female', 'Platinum'),
(9, 'Rahul Das', 'Kolkata', 'West Bengal', 'Male', 'Silver'),
(10, 'Pooja Joshi', 'Pune', 'Maharashtra', 'Female', 'Gold');


insert into products values
(101, 'Smartphone', 'Electronics', 25000.00),
(102, 'Laptop', 'Electronics', 55000.00),
(103, 'Headphones', 'Electronics', 2000.00),
(104, 'T-Shirt', 'Fashion', 799.00),
(105, 'Jeans', 'Fashion', 1499.00),
(106, 'Washing Machine', 'Home Appliances', 18000.00),
(107, 'Mixer Grinder', 'Home Appliances', 3500.00),
(108, 'Book - SQL Basics', 'Books', 650.00),
(109, 'Office Chair', 'Furniture', 7000.00),
(110, 'Smart Watch', 'Electronics', 4500.00);

insert into orders values
(1001, 1, '2026-01-05', 'Delivered'),
(1002, 2, '2026-01-10', 'Shipped'),
(1003, 3, '2026-01-12', 'Delivered'),
(1004, 4, '2026-01-15', 'Cancelled'),
(1005, 5, '2026-01-18', 'Pending'),
(1006, 1, '2026-01-20', 'Delivered'),
(1007, 6, '2026-01-25', 'Delivered'),
(1008, 7, '2026-02-01', 'Pending'),
(1009, 8, '2026-02-03', 'Shipped'),
(1010, 9, '2026-02-08', 'Delivered'),
(1011, 10, '2026-02-12', 'Cancelled'),
(1012, 3, '2026-02-15', 'Delivered'),
(1013, 2, '2026-02-18', 'Pending'),
(1014, 4, '2026-02-22', 'Delivered'),
(1015, 5, '2026-02-25', 'Shipped');

insert into order_items values
(1, 1001, 101, 1),
(2, 1001, 103, 2),
(3, 1002, 104, 3),
(4, 1002, 105, 1),
(5, 1003, 102, 1),
(6, 1003, 108, 2),
(7, 1004, 110, 1),
(8, 1005, 107, 1),
(9, 1005, 108, 1),
(10, 1006, 104, 2),
(11, 1006, 110, 1),
(12, 1007, 106, 1),
(13, 1008, 103, 1),
(14, 1008, 104, 2),
(15, 1009, 109, 1),
(16, 1010, 105, 2),
(17, 1011, 102, 1),
(18, 1012, 101, 1),
(19, 1012, 110, 2),
(20, 1013, 108, 3),
(21, 1014, 106, 1),
(22, 1014, 107, 1),
(23, 1015, 103, 2),
(24, 1015, 104, 1);

insert into payments values
(201, 1001, 'Upi', 'Successful', 29000.00),
(202, 1002, 'Credit Card', 'Successful', 3896.00),
(203, 1003, 'Net Banking', 'Successful', 56300.00),
(204, 1004, 'Upi', 'Successful', 4500.00),
(205, 1005, 'Cash on Delivery', 'Pending', 4150.00),
(206, 1006, 'Debit Card', 'Successful', 6098.00),
(207, 1007, 'Upi', 'Successful', 18000.00),
(208, 1008, 'Upi', 'Failed', 3598.00),
(209, 1009, 'Credit Card', 'Successful', 7000.00),
(210, 1010, 'Debit Card', 'Successful', 0.00),
(211, 1011, 'Net Banking', 'Failed', null),
(212, 1012, 'Upi', 'Successful', 34000.00),
(213, 1013, 'Cash on Delivery', 'Pending', 1950.00),
(214, 1014, 'Upi', 'Successful', 21500.00),
(215, 1015, 'Credit Card', 'Successful', 0.00);

insert into deliveries values
(301, 1001, 'Delhivery', 'Delivered', 'Hyderabad'),
(302, 1002, 'Blue Dart', 'In Transit', 'Chennai'),
(303, 1003, 'Ecom Express', 'Delivered', 'Mumbai'),
(304, 1004, 'Shadowfax', 'Cancelled', 'Bangalore'),
(305, 1005, 'Delhivery', 'Pending', 'Hyderabad'),
(306, 1006, 'Blue Dart', 'Delivered', 'Hyderabad'),
(307, 1007, 'Ecom Express', 'Delivered', 'Kochi'),
(308, 1008, 'Shadowfax', 'Pending', 'Chennai'),
(309, 1009, 'Delhivery', 'In Transit', 'Delhi'),
(310, 1010, 'Blue Dart', 'Delivered', 'Kolkata'),
(311, 1011, 'Ecom Express', 'Cancelled', 'Pune'),
(312, 1012, 'Shadowfax', 'Delivered', 'Mumbai'),
(313, 1013, 'Delhivery', 'Pending', 'Chennai'),
(314, 1014, 'Blue Dart', 'Delivered', 'Bangalore'),
(315, 1015, 'Ecom Express', 'In Transit', 'Hyderabad');

--  1: 
select * from customers;

--  2: 
select customer_name,city,membership_type from customers;

--  3: 
select * from products order by price desc;

--  4:
select * from customers  where city='Hyderabad';

--  5:
select * from customers  where membership_type='Gold';

--  6:
select * from products where price between 500 and 5000;

--  7:
select * from products where category in ('Electronics','Fashion');

--  8: 
select * from orders where order_date >'2026-01-01';

-- 9:
select * from payments where payment_mode='Upi';

-- 10:
select * from deliveries where delivery_status='Pending';

-- 11:
select count(*) as Total_Customers from customers;

-- 12:
select count(*) as Total_orders from orders;

-- 13:
 select count(*) as Total_products from products;

-- 14:
select sum(amount) as Total_revenue from payments 
where payment_status='Successful';

-- 15:
select avg(amount) as Average_amount from payments;

-- 16:
select max(amount) as Highest_payment from payments;

-- 17:
select min(amount) as Lowest_payment from payments;

-- 18:
select city,count(*) as Total_customers from customers
group by city;

-- 19:
select category,count(*) as Total_Products from products
group by category;

-- 20:
select order_status,count(*) as Total_orders from orders
group by order_status;

-- 21:
select c.customer_name, o.order_id, o.order_date from customers c
join orders o on c.customer_id=o.customer_id;

-- 22:
select o.order_id, p.product_name, o.quantity, p.price
from order_items o
join products p on o.product_id = p.product_id;

-- 23:
select 
	c.customer_name, 
    p.product_name, 
    oi.quantity, 
    o.order_date from customers c
join orders o on c.customer_id = o.customer_id
join order_items oi on o.order_id = oi.order_id
join products p on oi.product_id = p.product_id;

-- 24:
select 
	o.order_id,
    p.payment_mode,
    p.payment_status,  
	p.amount from payments p
join orders o on o.order_id=p.order_id;

-- 25:
select 
	o.order_id,
    d.delivery_partner,
    d.delivery_status from deliveries d
join orders o on o.order_id=d.order_id;

-- 26:
select
    c.customer_name,
    c.city,
    o.order_id,
    o.order_date,
    p.product_name,
    p.category,
    oi.quantity,
    p.price,
    pay.payment_status,
    d.delivery_status
from customers c
join orders o on c.customer_id = o.customer_id
join order_items oi on o.order_id = oi.order_id
join products p on oi.product_id = p.product_id
join payments pay on o.order_id = pay.order_id
join deliveries d on o.order_id = d.order_id;

-- 27:
select c.city, sum(p.amount) as Total_revenue from customers c
join orders o on c.customer_id = o.customer_id
join payments p on o.order_id = p.order_id
where p.payment_status = 'Successful'
group by c.city;

-- 28:
select c.customer_name, sum(p.amount) as Total_revenue from customers c
join orders o on c.customer_id = o.customer_id
join payments p on o.order_id = p.order_id
where p.payment_status = 'Successful'
group by c.customer_name;

-- 29:
select 
	p.product_name, 
	sum(oi.quantity) as total_quantity_sold
	from products p
join order_items oi on p.product_id = oi.product_id
group by p.product_name;

-- 30:
select 
	p.category, 
    sum(oi.quantity * p.price) as total_revenue
	from products p
join order_items oi on p.product_id = oi.product_id
group by p.category;

-- 31:
select 
	c.customer_name,
    count(o.order_id) AS Total_Orders from customers c
inner join orders o on c.customer_id =o.customer_id
group by c.customer_name;

-- 32:
select 
	c.customer_name,
    count(o.order_id) AS Total_Orders from customers c
inner join orders o on c.customer_id =o.customer_id
group by c.customer_name
having count(o.order_id) >1;

-- 33:
select
    p.category,
    sum(oi.quantity * p.price) as total_revenue
from products p
join order_items oi on p.product_id = oi.product_id
group by p.category
having sum(oi.quantity * p.price) > 10000;

-- 34:
select city, count(*) as total_customers
from customers
group by city having count(*) > 2;

-- 35:
select p.product_name, sum(oi.quantity) as total_sold
from products p
join order_items oi on p.product_id = oi.product_id
group by p.product_name
having sum(oi.quantity) > 3;

-- 36:
select * from customers
where customer_id in (select customer_id from orders);

-- 37:
select * from customers
where customer_id not in (select customer_id from orders);

-- 38:
select * from products
where product_id not in (select product_id from order_items);

-- 39:
select * from payments
where amount > (
    select avg(amount) from payments
);

-- 40:
select distinct c.customer_name, pay.amount from customers c
join orders o on c.customer_id = o.customer_id
join payments pay on o.order_id = pay.order_id
where pay.amount = (
    select max(amount) from payments
); 

-- 41:
select * from products
where price > (
	select avg(price) from products
);

-- 42:
select * from customers
where customer_id in (
    select o.customer_id
    from orders o
    where o.order_id in (
        select oi.order_id
        from order_items oi
        join products p on oi.product_id = p.product_id
        where p.category = 'Electronics'
    )
);

-- 43:
select * from orders 
where order_id in (
	select order_id from payments 
    where payment_status ='Successful'
);

-- 44:
select * from orders 
where order_id in (
	select order_id from deliveries 
    where delivery_status ='Pending'
);

-- 45:
select 
	c.customer_id, 
    c.customer_name, 
    sum(pay.amount) as total_spending
from customers c
join orders o on c.customer_id = o.customer_id
join payments pay on o.order_id = pay.order_id
where pay.payment_status = 'Successful'
group by c.customer_id, c.customer_name
having sum(pay.amount) > (
    select avg(customer_total)
    from (
        select sum(pay2.amount) as customer_total
        from customers c2
        join orders o2 on c2.customer_id = o2.customer_id
        join payments pay2 on o2.order_id = pay2.order_id
        where pay2.payment_status = 'Successful'
        group by c2.customer_id
    ) as avg_spending
);

-- 46:
select * from orders
where order_id not in (
    select order_id from payments
);

-- 47:
select * from orders
where order_id not in (
    select order_id from deliveries
);

-- 48:
select * from payments
where amount is null or amount = 0;

-- 49:
select 
	o.order_id, 
    o.order_status, 
    p.payment_status
from orders o
join payments p on o.order_id = p.order_id
where o.order_status = 'Cancelled'
and p.payment_status = 'Successful';

-- 50:
select 
	o.order_id, 
    o.order_status, 
    p.payment_status
from orders o
join payments p on o.order_id = p.order_id
where o.order_status = 'Delivered'
and p.payment_status = 'Failed';

-- 51:
select oi.* from order_items oi
left join products p on oi.product_id = p.product_id
where p.product_id is null;

-- 52:
select o.* from orders o
left join customers c on o.customer_id = c.customer_id
where c.customer_id is null;
