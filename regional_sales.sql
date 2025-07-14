SELECT Region, SUM(Sales) AS RegionSales
FROM sales
GROUP BY Region
ORDER BY RegionSales DESC;
