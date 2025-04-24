from mcp.server.fastmcp import FastMCP
from typing import List
from collections import Counter
from datetime import datetime, timedelta
import json

# In-memory mock datasets for restaurant management
sales_data = [
    {"dish": "Burger", "date": "2025-04-24"},
    {"dish": "Pasta", "date": "2025-04-24"},
    {"dish": "Burger", "date": "2025-04-24"},
    {"dish": "Pizza", "date": "2025-04-24"},
    {"dish": "Pizza", "date": "2025-04-23"}
]

inventory_data = [
    {"item": "Tomatoes", "quantity": 10},
    {"item": "Cheese", "quantity": 5},
    {"item": "Pasta", "quantity": 50},
    {"item": "Burger Buns", "quantity": 15}
]

staff_data = [
    {"name": "Alice", "availability": ["Monday", "Tuesday", "Wednesday"]},
    {"name": "Bob", "availability": ["Thursday", "Friday", "Saturday"]},
    {"name": "Charlie", "availability": ["Friday", "Saturday", "Sunday"]}
]

feedback_data = [
    {"date": "2025-04-23", "feedback": "Loved the pizza!"},
    {"date": "2025-04-23", "feedback": "Service was a bit slow."},
    {"date": "2025-04-22", "feedback": "Great ambiance!"}
]

# Create MCP server
mcp = FastMCP("RestaurantManager")

@mcp.tool()
def best_selling_items():
    today = datetime.now().strftime('%Y-%m-%d')
    today_sales = [entry['dish'] for entry in sales_data if entry['date'] == today]
    count = Counter(today_sales)
    return count.most_common(3)

@mcp.tool()
def get_low_stock_items(threshold: int = 20):
    return [item for item in inventory_data if item['quantity'] < threshold]

@mcp.tool()
def suggest_staff_schedule():
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%A')
    available_staff = [s['name'] for s in staff_data if tomorrow in s['availability']]
    return {"day": tomorrow, "available_staff": available_staff}

@mcp.tool()
def add_inventory_item(item: str, quantity: int):
    found = False
    for entry in inventory_data:
        if entry['item'].lower() == item.lower():
            entry['quantity'] += quantity
            found = True
            break
    if not found:
        inventory_data.append({"item": item, "quantity": quantity})
    return {"status": "success", "item": item, "new_quantity": quantity}

@mcp.tool()
def summarize_yesterdays_feedback():
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    feedbacks = [entry['feedback'] for entry in feedback_data if entry['date'] == yesterday]
    return {"date": yesterday, "feedback_summary": feedbacks if feedbacks else "No feedback recorded."}

if __name__ == "__main__":
    mcp.run()
