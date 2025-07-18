print("=== NIGERIAN E-COMMERCE FINAL ANALYSIS ===")
print()

# Your data
products = ["Phone", "Laptop", "Tablet", "Headphones", "Power Bank", "Charger"]
prices = [50000, 150000, 80000, 25000, 15000, 5000]
quantities = [10, 5, 8, 15, 20, 25]
states = ["Lagos", "Abuja", "Kano", "Lagos", "Port Harcourt", "Ibadan"]

# Calculate everything
revenues = []
total_revenue = 0
for i in range(len(products)):
    revenue = prices[i] * quantities[i]
    revenues.append(revenue)
    total_revenue += revenue

print("📊 PRODUCT PERFORMANCE:")
print("=" * 60)
for i in range(len(products)):
    stars = "*" * (quantities[i] // 2)
    print(f"{products[i]:12} | ₦{prices[i]:8,} | Qty: {quantities[i]:2} | {stars}")

print()
print("💰 BUSINESS SUMMARY:")
print("=" * 40)
print(f"Total Revenue: ₦{total_revenue:,}")
print(f"Total Products: {len(products)}")
print(f"Best Seller: {products[quantities.index(max(quantities))]}")
print(f"Most Expensive: {products[prices.index(max(prices))]}")

print()
print("🏙️ NIGERIAN STATES ANALYSIS:")
print("=" * 40)
state_revenue = {}
for i in range(len(states)):
    state = states[i]
    revenue = revenues[i]
    if state in state_revenue:
        state_revenue[state] += revenue
    else:
        state_revenue[state] = revenue

for state, revenue in state_revenue.items():
    print(f"{state}: ₦{revenue:,}")

print()
print("🎯 KEY INSIGHTS:")
print("=" * 30)
print("• Lagos has the highest revenue potential")
print("• Phones and Laptops are premium products") 
print("• Power Banks and Chargers are volume sellers")
print("• 6 product categories across 5 Nigerian states")

print()
print("✅ PROJECT COMPLETE!")
print("Nigerian E-commerce ETL & Analytics Pipeline Successfully Built!")git branch -M main
git push -u origin main