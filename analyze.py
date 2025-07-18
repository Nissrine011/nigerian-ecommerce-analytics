import csv

print("🚀 Nigerian E-commerce Analysis")
print("=" * 40)

# Read data
orders = []
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        orders.append(row)

print(f"📊 Loaded {len(orders)} orders")

# Calculate totals
total_revenue = 0
city_sales = {}
product_sales = {}

for order in orders:
    revenue = int(order['total'])
    city = order['city']
    product = order['product']
    
    total_revenue += revenue
    
    if city in city_sales:
        city_sales[city] += revenue
    else:
        city_sales[city] = revenue
    
    if product in product_sales:
        product_sales[product] += revenue
    else:
        product_sales[product] = revenue

# Results
print(f"\n💰 Total Revenue: ₦{total_revenue:,}")
print(f"📦 Total Orders: {len(orders)}")

print("\n🏆 TOP CITIES:")
for city, sales in sorted(city_sales.items(), key=lambda x: x[1], reverse=True):
    print(f"• {city}: ₦{sales:,}")

print("\n📱 TOP PRODUCTS:")
for product, sales in sorted(product_sales.items(), key=lambda x: x[1], reverse=True):
    print(f"• {product}: ₦{sales:,}")

print("\n✅ Analysis Complete!")
