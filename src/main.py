# main.py
# A simple script to demonstrate the Food Monitoring System.

# Sample food data
food_data = [
    {"name": "Milk", "temperature": 8, "expiration_days": 3},
    {"name": "Meat", "temperature": 5, "expiration_days": 1},
    {"name": "Vegetables", "temperature": 10, "expiration_days": 5},
]

# Thresholds
ALERT_THRESHOLD = 7  # Maximum safe temperature in Celsius
EXPIRATION_LIMIT = 1  # Minimum days to expiration

# Function to check food safety
def check_food_safety(data):
    """
    Checks each food item's safety based on temperature and expiration days.

    Args:
        data (list of dict): Food items with attributes 'name', 'temperature', and 'expiration_days'.

    Returns:
        list: Alerts for items that exceed safety thresholds.
    """
    alerts = []
    for item in data:
        # Validate data
        try:
            name = item["name"]
            temperature = item["temperature"]
            expiration_days = item["expiration_days"]
        except KeyError as e:
            alerts.append(f"ERROR: Missing key {e} in item {item}")
            continue

        # Check safety conditions
        if temperature > ALERT_THRESHOLD:
            alerts.append(f"ALERT: {name} exceeds safe temperature! (Temp: {temperature}°C)")
        if expiration_days <= EXPIRATION_LIMIT:
            alerts.append(f"ALERT: {name} is near expiration! (Days left: {expiration_days})")
    return alerts

# Main function
if __name__ == "__main__":
    print("Food Monitoring System - Simple Version")
    print("=" * 40)
    
    # Display food data
    print("\nFood Data:")
    for item in food_data:
        print(f"- {item['name']}: Temp={item['temperature']}°C, Expiration={item['expiration_days']} days")

    # Generate and display alerts
    alerts = check_food_safety(food_data)
    print("\nSystem Alerts:")
    if alerts:
        for alert in alerts:
            print(alert)
    else:
        print("No issues detected. All items are safe!")
