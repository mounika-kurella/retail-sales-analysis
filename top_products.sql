SELECT ProductName, SUM(Sales) AS TotalSales
FROM sales
GROUP BY ProductName
ORDER BY TotalSales DESC
LIMIT 10;
