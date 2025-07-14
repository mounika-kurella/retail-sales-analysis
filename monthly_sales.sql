SELECT strftime('%Y-%m', OrderDate) AS Month, SUM(Sales) AS MonthlyRevenue
FROM sales
GROUP BY Month
ORDER BY Month;
