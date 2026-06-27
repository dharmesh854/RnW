CREATE DATABASE Practical_Test;

USE Practical_Test;

CREATE TABLE Products(
Product_ID INT PRIMARY KEY,
Name VARCHAR(50),
Category_ID INT UNIQUE KEY,
FOREIGN KEY (Category_ID) REFERENCES Categories(Category_ID),
Price DECIMAL,
Stock_Quantity INT,
Added_Date DATE
);

CREATE TABLE Categories(
Category_ID INT PRIMARY KEY,
Category_Name VARCHAR(60)
);

CREATE TABLE Customers(
Customer_ID INT PRIMARY KEY,
Customer_Name VARCHAR(50),
Email VARCHAR(50),
Phone_Number BIGINT,
Address VARCHAR(70),
Registration_Date DATE
);

CREATE TABLE Orders(
Order_ID INT PRIMARY KEY,
Customer_ID INT,
FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
Order_Date DATE,
Total_Amount DECIMAL,
Order_Status VARCHAR(50)
);

CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    quantity INT,
    subtotal DECIMAL(10,2)
);

CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    payment_date DATE,
    payment_method VARCHAR(20),
    payment_status VARCHAR(20)
);

CREATE TABLE Shipping (
    shipping_id INT PRIMARY KEY,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    shipping_date DATE,
    delivery_date DATE,
    shipping_status VARCHAR(20)
);
 
INSERT INTO Categories VALUES
(1,'Electronics'),
(2,'Clothing'),
(3,'Books'),
(4,'Furniture'),
(5,'Groceries'),
(6,'Sports'),
(7,'Beauty'),
(8,'Toys');

INSERT INTO Products VALUES
(101,'Mobile Phone',1,15000,50,'2024-01-18'),
(102,'Laptop',2,55000,20,'2023-12-28'),
(103,'T-Shirt',3,800,100,'2024-01-07'),
(104,'Novel Book',4,500,70,'2024-01-25'),
(105,'Sofa',5,25000,10,'2023-12-30'),
(106,'Rice Bag',6,1200,40,'2024-01-12'),
(107,'Cricket Bat',7,3000,25,'2024-01-03'),
(108,'Toy Car',8,600,60,'2024-01-20');

INSERT INTO Customers VALUES
(1,'Rahul Sharma','rahul@gmail.com',9876543210,'Delhi','2024-01-15'),
(2,'Amit Patel','amit@gmail.com',9123456780,'Ahmedabad','2023-12-29'),
(3,'Neha Verma','neha@gmail.com',9988776655,'Mumbai','2024-01-06'),
(4,'Pooja Singh','pooja@gmail.com',9090909090,'Jaipur','2024-01-22'),
(5,'Rohit Mehta','rohit@gmail.com',9012345678,'Surat','2023-12-31'),
(6,'Kiran Joshi','kiran@gmail.com',9345678901,'Rajkot','2024-01-10'),
(7,'Ankit Shah','ankit@gmail.com',9765432109,'Vadodara','2024-01-02'),
(8,'Sneha Kulkarni','sneha@gmail.com',7854123690,'Pune','2024-01-18');

INSERT INTO Orders VALUES
(201,1,'2024-02-10',15000,'Placed'),
(202,2,'2024-01-28',55000,'Shipped'),
(203,3,'2024-02-18',800,'Delivered'),
(204,4,'2024-01-30',500,'Placed'),
(205,5,'2024-02-12',25000,'Cancelled'),
(206,6,'2024-01-25',1200,'Delivered'),
(207,7,'2024-02-20',3000,'Shipped'),
(208,8,'2024-01-18',600,'Placed');

INSERT INTO Order_Items VALUES
(1,201,101,1,15000),
(2,202,102,1,55000),
(3,203,103,1,800),
(4,204,104,1,500),
(5,205,105,1,25000),
(6,206,106,1,1200),
(7,207,107,1,3000),
(8,208,108,1,600);

INSERT INTO Payments VALUES
(301,201,'2024-02-09','UPI','Paid'),
(302,202,'2024-01-27','Credit Card','Paid'),
(303,203,'2024-02-17','PayPal','Paid'),
(304,204,'2024-01-29','UPI','Pending'),
(305,205,'2024-02-11','Debit Card','Failed'),
(306,206,'2024-01-24','UPI','Paid'),
(307,207,'2024-02-19','Credit Card','Paid'),
(308,208,'2024-01-17','UPI','Pending');

INSERT INTO Shipping VALUES
(401,201,'2024-02-10','2024-02-15','Delivered'),
(402,202,'2024-01-28','2024-02-03','In Transit'),
(403,203,'2024-02-18','2024-02-22','Delivered'),
(404,204,'2024-01-30',NULL,'Dispatched'),
(405,205,'2024-02-12',NULL,'Cancelled'),
(406,206,'2024-01-25','2024-01-30','Delivered'),
(407,207,'2024-02-20','2024-02-25','In Transit'),
(408,208,'2024-01-18',NULL,'Dispatched');



-- Insert new Products, Customers and Orders 
INSERT INTO Categories VALUES
(9,'Electronics'),
(10,'Clothing');

INSERT INTO Products VALUES
(109,'Smart Watch',9,5000,30,'2024-03-01'),
(110,'Headphones',10,2500,45,'2024-03-02');

INSERT INTO Customers VALUES
(9,'Vikas Kumar','vikas@gmail.com',9123456701,'Noida','2024-03-01'),
(10,'Riya Malhotra','riya@gmail.com',9026534855,'Chandigarh','2024-03-02');

INSERT INTO Orders VALUES
(209,9,'2024-03-05',5000,'Placed'),
(210,10,'2024-03-06',2500,'Placed');

-- Update stock when an order is placed
UPDATE Products SET Stock_Quantity = Stock_Quantity - 1 WHERE Product_ID = 101;

-- Select orders cancelled more than 30 days ago
SELECT * FROM Orders
WHERE Order_Status = 'Cancelled'
AND Order_Date < DATE_SUB(CURDATE(), INTERVAL 30 DAY);

--  Find all orders placed in Last 6 months
SELECT * FROM Orders WHERE Order_Date >= '2023-08-01';

-- Get top 5 highest priced products
SELECT * FROM Products ORDER BY Price DESC LIMIT 5;

-- Customers who placed more than 3 orders
SELECT Customer_ID, COUNT(Order_ID) AS Total_Orders FROM Orders
GROUP BY Customer_ID HAVING COUNT(Order_ID) > 3;

-- Orders with status = Pending AND payment = Paid
SELECT o.Order_ID, o.Order_Status, p.Payment_Status FROM Orders o
JOIN Payments p ON o.Order_ID = p.Order_ID WHERE o.Order_Status = 'Placed' AND p.Payment_Status = 'Paid';

-- Products that are NOT out of stock
SELECT * FROM Products WHERE NOT Stock_Quantity = 0;

-- Customers registered after 2022 OR purchases above ₹10,000
SELECT DISTINCT c.Customer_ID, c.Customer_Name FROM Customers c
JOIN Orders o ON c.Customer_ID = o.Customer_ID WHERE c.Registration_Date > '2022-12-31' OR o.Total_Amount > 10000;

-- Products sorted by price (descending)
SELECT * FROM Products ORDER BY Price DESC;

-- Number of orders placed by each customer
SELECT Customer_ID, COUNT(Order_ID) AS Order_Count FROM Orders GROUP BY Customer_ID;

-- Total revenue generated per category
SELECT c.Category_Name, SUM(p.Price) AS Total_Revenue FROM Products p
JOIN Categories c ON p.Category_ID = c.Category_ID GROUP BY c.Category_Name;

-- Total revenue of store
SELECT SUM(Total_Amount) AS Total_Revenue FROM Orders;

-- Most purchased product
SELECT product_id, COUNT(product_id) AS Purchase_Count FROM Order_Items
GROUP BY product_id ORDER BY Purchase_Count DESC LIMIT 1;

-- Average order value
SELECT AVG(Total_Amount) AS Average_Order_Value FROM Orders;

-- Products with their category names (INNER JOIN)
SELECT p.Product_ID, p.Name, c.Category_Name FROM Products p
INNER JOIN Categories c ON p.Category_ID = c.Category_ID;

-- All orders with customer details (LEFT JOIN)
SELECT o.Order_ID, c.Customer_Name, o.Total_Amount, o.Order_Status FROM Customers c
LEFT JOIN Orders o ON c.Customer_ID = o.Customer_ID;

-- Orders that haven’t been shipped (RIGHT JOIN)
SELECT o.Order_ID, s.Shipping_Status FROM Orders o
RIGHT JOIN Shipping s ON o.Order_ID = s.Order_ID WHERE s.Shipping_Status != 'Delivered';

-- Customers who never placed an order (FULL OUTER JOIN)
SELECT c.Customer_ID, c.Customer_Name FROM Customers c
LEFT JOIN Orders o ON c.Customer_ID = o.Customer_ID
WHERE o.Order_ID IS NULL;

-- Orders placed by customers registered after 2022
SELECT * FROM Orders WHERE Customer_ID IN (SELECT Customer_ID
FROM Customers WHERE Registration_Date > '2022-12-31');

-- Customer who has spent the most
SELECT Customer_ID, SUM(Total_Amount) AS Total_Spent FROM Orders
GROUP BY Customer_ID ORDER BY Total_Spent DESC LIMIT 1;

-- Products that have never been ordered
SELECT * FROM Products WHERE Product_ID NOT IN (SELECT Product_ID FROM Order_Items);

-- Count orders per month
SELECT MONTH(Order_Date) AS Order_Month, COUNT(*) AS Total_Orders FROM Orders GROUP BY MONTH(Order_Date);

-- Delivery time (difference between shipping & delivery)
SELECT Order_ID, DATEDIFF(Delivery_Date, Shipping_Date) AS Delivery_Days FROM Shipping WHERE Delivery_Date IS NOT NULL;

-- Format order date as DD-MM-YYYY
SELECT Order_ID, DATE_FORMAT(Order_Date, '%d-%m-%Y') AS Formatted_Date FROM Orders;

-- Convert product names to uppercase
SELECT UPPER(Name) AS Product_Name FROM Products;

-- Trim spaces from customer names
SELECT TRIM(Customer_Name) AS Clean_Name FROM Customers;

-- Replace missing email with "Not Provided"
SELECT Customer_Name, IFNULL(Email, 'Not Provided') AS Email FROM Customers;

-- Rank customers based on total spending
SELECT Customer_ID, SUM(Total_Amount) AS Total_Spent,
RANK() OVER (ORDER BY SUM(Total_Amount) DESC) AS Rank_No FROM Orders GROUP BY Customer_ID;

-- Cumulative total revenue per month
SELECT MONTH(Order_Date) AS Month, SUM(Total_Amount) AS Monthly_Revenue,
SUM(SUM(Total_Amount)) OVER (ORDER BY MONTH(Order_Date)) AS Cumulative_Revenue FROM Orders GROUP BY MONTH(Order_Date);

-- Running total of orders
SELECT Order_ID, COUNT(Order_ID) OVER (ORDER BY Order_Date) AS Running_Orders FROM Orders;

-- Assign Loyalty Status to customers
SELECT Customer_ID, SUM(Total_Amount) AS Total_Spent,
CASE
    WHEN SUM(Total_Amount) > 50000 THEN 'Gold'
    WHEN SUM(Total_Amount) BETWEEN 20000 AND 50000 THEN 'Silver'
    ELSE 'Bronze'
END AS Loyalty_Status FROM Orders GROUP BY Customer_ID;

-- Categorize products
SELECT Product_ID, SUM(Quantity) AS Total_Sold,
CASE
    WHEN SUM(Quantity) > 500 THEN 'Best Seller'
    WHEN SUM(Quantity) BETWEEN 200 AND 500 THEN 'Popular'
    ELSE 'Regular'
END AS Product_Status FROM Order_Items GROUP BY Product_ID;















