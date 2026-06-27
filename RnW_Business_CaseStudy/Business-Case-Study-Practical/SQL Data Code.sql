Create database Practical_b_Casestudy;

Use Practical_b_Casestudy;

CREATE TABLE RetailTransactions (
    TransactionID VARCHAR(20),
    Date DATE,
    ProductName VARCHAR(50),
    Category VARCHAR(50),
    Region VARCHAR(20),
    SalesChannel VARCHAR(20),
    Quantity INT,
    UnitPrice INT,
    TotalAmount INT,
    PaymentMode VARCHAR(20),
    CustomerID VARCHAR(10) 
);

INSERT INTO RetailTransactions VALUES
('T001','2025-01-05','Mobile','Electronics','North','Online',2,15000,30000,'UPI','C101'),
('T002','2025-01-07','Laptop','Electronics','West','Offline',1,55000,55000,'Credit Card','C102'),
('T003','2025-01-10','Shoes','Fashion','South','Online',3,2000,6000,'Cash','C103'),
('T004','2025-01-12','Watch','Accessories','East','Offline',2,3000,6000,'UPI','C104'),
('T005','2025-01-15','T-shirt','Fashion','North','Online',5,500,2500,'Net Banking','C105'),
('T006','2025-01-18','Headphones','Electronics','West','Online',2,2500,5000,'UPI','C106'),
('T007','2025-01-20','Bag','Accessories','South','Offline',1,1500,1500,'Cash','C107'),
('T008','2025-01-22','Tablet','Electronics','East','Online',1,20000,20000,'Credit Card','C108'),
('T009','2025-01-25','Jeans','Fashion','North','Offline',2,1800,3600,'UPI','C109'),
('T010','2025-01-28','Sunglasses','Accessories','West','Online',3,1200,3600,'Net Banking','C110'),

('T011','2025-02-02','Mobile','Electronics','South','Online',1,14000,14000,'UPI','C101'),
('T012','2025-02-05','Laptop','Electronics','East','Offline',1,60000,60000,'Credit Card','C102'),
('T013','2025-02-08','Shoes','Fashion','North','Online',2,2200,4400,'Cash','C103'),
('T014','2025-02-10','Watch','Accessories','West','Offline',1,3500,3500,'UPI','C104'),
('T015','2025-02-12','T-shirt','Fashion','South','Online',4,600,2400,'Net Banking','C105'),
('T016','2025-02-15','Headphones','Electronics','East','Online',3,2000,6000,'UPI','C106'),
('T017','2025-02-18','Bag','Accessories','North','Offline',2,1800,3600,'Cash','C107'),
('T018','2025-02-20','Tablet','Electronics','West','Online',1,22000,22000,'Credit Card','C108'),
('T019','2025-02-22','Jeans','Fashion','South','Offline',3,2000,6000,'UPI','C109'),
('T020','2025-02-25','Sunglasses','Accessories','East','Online',2,1500,3000,'Net Banking','C110'),

('T021','2025-03-01','Mobile','Electronics','North','Offline',1,16000,16000,'Cash','C111'),
('T022','2025-03-03','Laptop','Electronics','South','Online',2,52000,104000,'UPI','C112'),
('T023','2025-03-05','Shoes','Fashion','West','Offline',4,1800,7200,'Net Banking','C113'),
('T024','2025-03-07','Watch','Accessories','North','Online',2,4000,8000,'Credit Card','C114'),
('T025','2025-03-10','T-shirt','Fashion','East','Offline',6,700,4200,'Cash','C115'),
('T026','2025-03-12','Headphones','Electronics','South','Online',2,3000,6000,'UPI','C116'),
('T027','2025-03-15','Bag','Accessories','West','Offline',3,1700,5100,'Cash','C117'),
('T028','2025-03-18','Tablet','Electronics','North','Online',1,25000,25000,'Credit Card','C118'),
('T029','2025-03-20','Jeans','Fashion','East','Offline',2,2100,4200,'UPI','C119'),
('T030','2025-03-22','Sunglasses','Accessories','South','Online',5,1300,6500,'Net Banking','C120'),

('T031','2025-03-25','Mobile','Electronics','West','Online',2,15500,31000,'UPI','C121'),
('T032','2025-03-27','Laptop','Electronics','North','Offline',1,58000,58000,'Credit Card','C122'),
('T033','2025-03-29','Shoes','Fashion','South','Online',3,1900,5700,'Cash','C123'),
('T034','2025-04-01','Watch','Accessories','East','Offline',2,3200,6400,'UPI','C124'),
('T035','2025-04-03','T-shirt','Fashion','West','Online',4,550,2200,'Net Banking','C125'),
('T036','2025-04-05','Headphones','Electronics','North','Online',1,2800,2800,'UPI','C126'),
('T037','2025-04-07','Bag','Accessories','South','Offline',2,1600,3200,'Cash','C127'),
('T038','2025-04-09','Tablet','Electronics','East','Online',1,23000,23000,'Credit Card','C128'),
('T039','2025-04-11','Jeans','Fashion','West','Offline',3,1900,5700,'UPI','C129'),
('T040','2025-04-13','Sunglasses','Accessories','North','Online',2,1400,2800,'Net Banking','C130'),

('T041','2025-04-15','Mobile','Electronics','South','Online',1,17000,17000,'UPI','C131'),
('T042','2025-04-17','Laptop','Electronics','East','Offline',1,62000,62000,'Credit Card','C132'),
('T043','2025-04-19','Shoes','Fashion','North','Online',2,2100,4200,'Cash','C133'),
('T044','2025-04-21','Watch','Accessories','West','Offline',1,3600,3600,'UPI','C134'),
('T045','2025-04-23','T-shirt','Fashion','South','Online',5,650,3250,'Net Banking','C135'),
('T046','2025-04-25','Headphones','Electronics','East','Online',2,2700,5400,'UPI','C136'),
('T047','2025-04-27','Bag','Accessories','North','Offline',3,1800,5400,'Cash','C137'),
('T048','2025-04-29','Tablet','Electronics','West','Online',1,24000,24000,'Credit Card','C138'),
('T049','2025-05-01','Jeans','Fashion','South','Offline',2,2000,4000,'UPI','C139'),
('T050','2025-05-03','Sunglasses','Accessories','East','Online',4,1500,6000,'Net Banking','C140');


-- QUERIES:

-- 1. Total sales amount per region for the last quarter.
SELECT Region, SUM(TotalAmount) AS TotalSales
FROM RetailTransactions
WHERE Date BETWEEN '2025-02-01' AND '2025-04-30'
GROUP BY Region;

-- 2. Top 5 best-selling products (by revenue).
SELECT ProductName, SUM(TotalAmount) AS Revenue
FROM RetailTransactions
GROUP BY ProductName
ORDER BY Revenue DESC
LIMIT 5;

-- 3. Monthly sales trend across all regions.
SELECT 
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    SUM(TotalAmount) AS MonthlySales
FROM RetailTransactions
GROUP BY Month
ORDER BY Month;

-- 4. Region-wise contribution to total sales (as a %).
SELECT 
    Region,
    SUM(TotalAmount) AS RegionSales,
    ROUND(SUM(TotalAmount) * 100 / (SELECT SUM(TotalAmount) FROM RetailTransactions), 2) AS PercentageContribution
FROM RetailTransactions
GROUP BY Region;

-- 5. Online vs Offline Sales Comparison
SELECT 
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    SalesChannel,
    SUM(TotalAmount) AS Sales
FROM RetailTransactions
GROUP BY Month, SalesChannel
ORDER BY Month;

-- 6. Sales trend by Category – Which categories are rising/falling?
SELECT 
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    Category,
    SUM(TotalAmount) AS Sales
FROM RetailTransactions
GROUP BY Month, Category
ORDER BY Month;

-- 7. List customers who purchased more than 10 times.
SELECT CustomerID, COUNT(*) AS PurchaseCount
FROM RetailTransactions
GROUP BY CustomerID
HAVING PurchaseCount > 10;


-- Store SQL outputs in a new sheet or table so they can be reused in visualization.

CREATE TABLE RegionSales AS
SELECT 
    Region,
    SUM(TotalAmount) AS TotalSales
FROM RetailTransactions
GROUP BY Region;



CREATE TABLE TopProducts AS
SELECT 
    ProductName,
    SUM(TotalAmount) AS Revenue
FROM RetailTransactions
GROUP BY ProductName
ORDER BY Revenue DESC;


CREATE TABLE MonthlySales AS
SELECT 
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    SUM(TotalAmount) AS TotalSales
FROM RetailTransactions
GROUP BY Month;


CREATE TABLE RegionContribution AS
SELECT 
    Region,
    SUM(TotalAmount) AS RegionSales,
    ROUND(SUM(TotalAmount) * 100 / 
        (SELECT SUM(TotalAmount) FROM RetailTransactions), 2
    ) AS PercentageContribution
FROM RetailTransactions
GROUP BY Region;



CREATE TABLE ChannelSales AS
SELECT 
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    SalesChannel,
    SUM(TotalAmount) AS Sales
FROM RetailTransactions
GROUP BY Month, SalesChannel;



CREATE TABLE CategorySales AS
SELECT 
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    Category,
    SUM(TotalAmount) AS Sales
FROM RetailTransactions
GROUP BY Month, Category;



CREATE TABLE FrequentCustomers AS
SELECT 
    CustomerID,
    COUNT(*) AS PurchaseCount
FROM RetailTransactions
GROUP BY CustomerID
HAVING PurchaseCount > 10;


CREATE TABLE DateTable AS
SELECT DISTINCT 
    Date,
    YEAR(Date) AS Year,
    MONTH(Date) AS Month,
    MONTHNAME(Date) AS MonthName,
    QUARTER(Date) AS Quarter,
    DAY(Date) AS Day,
    DAYNAME(Date) AS DayName
FROM RetailTransactions
ORDER BY Date;






 


