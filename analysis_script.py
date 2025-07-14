import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv('../data/orders.csv')
order_items = pd.read_csv('../data/order_items.csv')
products = pd.read_csv('../data/products.csv')

merged = order_items.merge(orders, on='order_id').merge(products, on='product_id')
merged['order_date'] = pd.to_datetime(merged['order_date'])
merged['sales'] = merged['quantity'] * merged['unit_price']
merged['month'] = merged['order_date'].dt.to_period('M')

monthly_sales = merged.groupby('month')['sales'].sum()

monthly_sales.plot(kind='line', title='Monthly Sales Trend')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()