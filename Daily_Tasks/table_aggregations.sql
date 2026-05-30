CREATE TABLE products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock_quantity INT,
    supplier_city VARCHAR(30)
);
 
 INSERT INTO products VALUES
(1,'Laptop','Electronics',55000,10,'Hyderabad'),
(2,'Mobile','Electronics',25000,25,'Bangalore'),
(3,'Printer','Electronics',18000,8,'Pune'),
(4,'Office Chair','Furniture',7500,15,'Mumbai'),
(5,'Desk','Furniture',12000,5,'Chennai'),
(6,'Notebook','Stationery',80,200,'Hyderabad'),
(7,'Pen','Stationery',20,500,'Delhi'),
(8,'Water Bottle','Accessories',500,50,'Bangalore');

select product_name,price from products;

select distinct category from products;

select * from products
where category ='Stationery';

select * from products
where price >5000;

select * from products
where category ='Stationery' and price >50;

select * from products
where supplier_city ='Bangalore' or supplier_city ='Hyderabad';

select * from products
where not category ='Stationery';

select * from products
where supplier_city in ('Bangalore','Hyderabad','Chennai');

select * from products
where price between 500 and  50000;

select * from products
where product_name like 'L%';

select * from products
where product_name like '%n';

select * from products
where product_name like '%ote%';

select product_name as Product ,price as Product_Price 
from products;

select * from products
order by price desc;

select count(*) as Total_Products from products;

select count(*) as No_Of_Rows from products
where category ='Stationery';

select sum(price) as Total_Price from products;

select 
count(*) as Total_Products,
sum(price) as Total_Price,
avg(price) as Average_Price,
max(price) as Highest_Price,
min(price) as Lowest_Price from products;

select category,count(*) as Product_count from products
group by category;

select category,sum(price) as Total_Price from products
group by category;
