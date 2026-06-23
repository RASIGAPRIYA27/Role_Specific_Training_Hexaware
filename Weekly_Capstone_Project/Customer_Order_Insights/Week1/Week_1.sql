CREATE DATABASE CustomerOrderDB;
USE CustomerOrderDB;

CREATE TABLE Customers(
customer_id INT PRIMARY KEY AUTO_INCREMENT,
customer_name VARCHAR(100) NOT NULL,
email VARCHAR(100),
phone VARCHAR(15),
city VARCHAR(50)
);

CREATE TABLE Orders(
order_id INT PRIMARY KEY AUTO_INCREMENT,
customer_id INT,
product_name VARCHAR(100),
quantity INT,
price DECIMAL(10,2),
order_date DATE,
FOREIGN KEY(customer_id)
REFERENCES Customers(customer_id)
);

CREATE TABLE Delivery_Status(
delivery_id INT PRIMARY KEY AUTO_INCREMENT,
order_id INT,
delivery_date DATE,
status VARCHAR(30),
expected_date DATE,
FOREIGN KEY(order_id)
REFERENCES Orders(order_id)
);

INSERT INTO Customers(customer_name,email,phone,city)
VALUES
('Arun','arun@gmail.com','9876543210','Chennai'),
('Meena','meena@gmail.com','9876543211','Bangalore'),
('Rahul','rahul@gmail.com','9876543212','Hyderabad'),
('Divya','divya@gmail.com','9876543213','Coimbatore'),
('Kiran','kiran@gmail.com','9876543214','Salem'),
('Sneha','sneha@gmail.com','9876543215','Madurai'),
('John','john@gmail.com','9876543216','Mumbai'),
('Priya','priya@gmail.com','9876543217','Delhi'),
('Akash','akash@gmail.com','9876543218','Pune'),
('Ravi','ravi@gmail.com','9876543219','Trichy');

INSERT INTO Orders(customer_id,product_name,quantity,price,order_date)
VALUES
(1,'Laptop',1,65000,'2026-06-01'),
(2,'Mouse',2,500,'2026-06-02'),
(3,'Keyboard',1,1200,'2026-06-03'),
(4,'Monitor',1,18000,'2026-06-03'),
(5,'Printer',1,15000,'2026-06-04'),
(6,'Tablet',2,25000,'2026-06-05'),
(7,'Smart Watch',1,12000,'2026-06-06'),
(8,'Headphones',2,3000,'2026-06-06'),
(9,'Power Bank',3,1500,'2026-06-07'),
(10,'USB Cable',5,300,'2026-06-07');

INSERT INTO Delivery_Status(order_id,delivery_date,status,expected_date)
VALUES
(1,'2026-06-03','Delivered','2026-06-03'),
(2,NULL,'Delayed','2026-06-04'),
(3,'2026-06-04','Delivered','2026-06-04'),
(4,NULL,'Delayed','2026-06-05'),
(5,'2026-06-06','Delivered','2026-06-06'),
(6,NULL,'In Transit','2026-06-08'),
(7,NULL,'Delayed','2026-06-08'),
(8,'2026-06-08','Delivered','2026-06-08'),
(9,NULL,'In Transit','2026-06-09'),
(10,'2026-06-08','Delivered','2026-06-08');

SELECT * FROM Customers;

SELECT * FROM Orders;

SELECT * FROM Delivery_Status;

INSERT INTO Orders(customer_id,product_name,quantity,price,order_date)
VALUES
(2,'Webcam',1,2500,'2026-06-09');

SET SQL_SAFE_UPDATES = 0;
UPDATE Orders
SET quantity=3
WHERE order_id=2;

DELETE FROM Orders
WHERE order_id=11;

SELECT * FROM Delivery_Status
WHERE status='Delivered';

SELECT * FROM Delivery_Status
WHERE status='Delayed';

SELECT * FROM Orders
WHERE price>10000;

SELECT * FROM Customers
WHERE city='Chennai';

SELECT
	c.customer_name,
	o.product_name,
	o.quantity,
	d.status,
	d.expected_date
	FROM Customers c
JOIN Orders o
ON c.customer_id=o.customer_id
JOIN Delivery_Status d
ON o.order_id=d.order_id;

SELECT COUNT(*) TotalCustomers
FROM Customers;

SELECT SUM(price*quantity) TotalSales
FROM Orders;

SELECT AVG(price) AveragePrice
FROM Orders;

SELECT MAX(price) HighestPrice
FROM Orders;

SELECT MIN(price) LowestPrice
FROM Orders;

SELECT status,COUNT(*) Orders
FROM Delivery_Status
GROUP BY status;

CREATE VIEW Customer_Order_View AS
SELECT
	c.customer_name,
	o.product_name,
	o.quantity,
	o.price,
	d.status
FROM Customers c
JOIN Orders o
ON c.customer_id=o.customer_id
JOIN Delivery_Status d
ON o.order_id=d.order_id;

SELECT * FROM Customer_Order_View;

DELIMITER $$

CREATE PROCEDURE GetDelayedDeliveries(
IN cust_id INT
)

BEGIN
SELECT
	c.customer_name,
	o.product_name,
	d.status,
	d.expected_date
FROM Customers c
JOIN Orders o
ON c.customer_id=o.customer_id
JOIN Delivery_Status d
ON o.order_id=d.order_id
WHERE
c.customer_id=cust_id AND d.status='Delayed';
END $$

DELIMITER ;

CALL GetDelayedDeliveries(2);

SELECT * FROM Orders
ORDER BY order_date DESC;

SELECT customer_id,COUNT(order_id) TotalOrders
FROM Orders
GROUP BY customer_id;

SELECT product_name,price
FROM Orders
ORDER BY price DESC
LIMIT 5;

SELECT * FROM Delivery_Status
WHERE status IN ('Delayed','In Transit');


