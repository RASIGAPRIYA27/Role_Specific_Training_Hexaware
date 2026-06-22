CREATE DATABASE SupplyChainDB;
USE SupplyChainDB;

CREATE TABLE Suppliers(
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100),
    city VARCHAR(50)
);

-- INVENTORY TABLE

CREATE TABLE Inventory(
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    quantity INT NOT NULL,
    reorder_level INT NOT NULL,
    price DECIMAL(10,2),
    supplier_id INT,
    FOREIGN KEY(supplier_id)
    REFERENCES Suppliers(supplier_id)
);

-- ORDERS TABLE

CREATE TABLE Orders(
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100),
    product_id INT,
    quantity INT,
    order_date DATE,
    status VARCHAR(30),
    FOREIGN KEY(product_id)
    REFERENCES Inventory(product_id)
);

-- INSERT INTO SUPPLIERS

INSERT INTO Suppliers
(supplier_name,contact_person,phone,email,city)
VALUES
('ABC Traders','Ramesh','9876543210','abc@gmail.com','Chennai'),
('Global Supplies','Priya','9876501234','global@gmail.com','Bangalore'),
('Fresh Foods Ltd','Kumar','9898989898','fresh@gmail.com','Hyderabad'),
('Tech Warehouse','David','9123456789','tech@gmail.com','Mumbai'),
('Elite Distributors','Suresh','9988776655','elite@gmail.com','Coimbatore');

-- INSERT INTO INVENTORY

INSERT INTO Inventory
(product_name,category,quantity,reorder_level,price,supplier_id)

VALUES

('Laptop','Electronics',45,20,65000,4),
('Mouse','Electronics',150,50,500,4),
('Keyboard','Electronics',90,40,1200,4),
('Rice Bag','Groceries',25,30,1200,3),
('Sugar','Groceries',80,40,60,3),
('Cooking Oil','Groceries',15,20,180,3),
('Printer','Electronics',18,10,15000,4),
('Monitor','Electronics',10,15,18000,4),
('Notebook','Stationery',300,100,40,5),
('Pen Pack','Stationery',500,200,120,5);

-- INSERT INTO ORDERS

INSERT INTO Orders
(customer_name,product_id,quantity,order_date,status)
VALUES
('Arun',1,2,'2026-06-01','Delivered'),
('Meena',2,5,'2026-06-02','Pending'),
('John',4,3,'2026-06-03','Delivered'),
('Akash',6,10,'2026-06-03','Pending'),
('Ravi',8,1,'2026-06-04','Shipped'),
('Priya',3,2,'2026-06-05','Delivered'),
('Divya',9,20,'2026-06-05','Pending'),
('Rahul',10,15,'2026-06-06','Delivered'),
('Kiran',5,10,'2026-06-06','Pending'),
('Sneha',7,1,'2026-06-07','Shipped');

SELECT * FROM Suppliers;

SELECT * FROM Inventory;

SELECT * FROM Orders;

INSERT INTO Suppliers
(supplier_name,contact_person,phone,email,city)
VALUES
('Metro Suppliers','Ajay','9000011111',
'metro@gmail.com','Delhi');

SET SQL_SAFE_UPDATES = 0;

UPDATE Inventory
SET quantity=120
WHERE product_name='Mouse';

DELETE FROM Orders WHERE order_id=10;

SELECT * FROM Inventory
WHERE quantity<reorder_level;

SELECT * FROM Orders
WHERE status='Pending';

SELECT * FROM Inventory
WHERE category='Electronics';

SELECT
	o.order_id,
	o.customer_name,
	i.product_name,
	o.quantity,
	o.status,
	s.supplier_name FROM Orders o
JOIN Inventory i
ON o.product_id=i.product_id
JOIN Suppliers s
ON i.supplier_id=s.supplier_id;

SELECT COUNT(*) AS TotalProducts
FROM Inventory;

SELECT AVG(price) AS AveragePrice
FROM Inventory;

SELECT MAX(price) FROM Inventory;

SELECT SUM(quantity*price) AS InventoryValue
FROM Inventory;

SELECT status,
COUNT(*) AS TotalOrders
FROM Orders
GROUP BY status;

CREATE VIEW Inventory_Status AS SELECT
	product_id,
	product_name,
	quantity,
	reorder_level,

CASE
WHEN quantity<reorder_level
THEN 'LOW STOCK'
ELSE 'AVAILABLE'
END AS Stock_Status
FROM Inventory;

SELECT * FROM Inventory_Status;

DELIMITER $$
CREATE PROCEDURE Auto_Reorder()
BEGIN
SELECT
i.product_id,
i.product_name,
i.quantity,
i.reorder_level,
s.supplier_name,
s.phone

FROM Inventory i
JOIN Suppliers s
ON i.supplier_id=s.supplier_id
WHERE i.quantity<i.reorder_level;
END $$
DELIMITER ;

CALL Auto_Reorder();

SELECT s.supplier_name,COUNT(i.product_id) AS Products
FROM Suppliers s
LEFT JOIN Inventory i
ON s.supplier_id=i.supplier_id
GROUP BY s.supplier_name;

SELECT product_name,price
FROM Inventory
ORDER BY price DESC
LIMIT 5;

SELECT * FROM Orders
ORDER BY order_date DESC;

SELECT SUM(quantity) AS TotalOrdered
FROM Orders;

SELECT i.product_name,i.price
FROM Inventory i
JOIN Suppliers s
ON i.supplier_id=s.supplier_id
WHERE s.supplier_name='Tech Warehouse';