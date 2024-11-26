# Food Monitoring System

## Overview
The Food Monitoring System is a simple Python-based project designed to ensure the safety of food items. It checks for unsafe conditions such as:
- High temperatures exceeding safe thresholds.
- Imminent expiration dates.

The system generates alerts to notify users of food items requiring immediate attention.

---

## Features
- **Safety Monitoring**: Checks for unsafe temperature levels and expiration dates.
- **Customizable Thresholds**: Adjust safety thresholds for temperature and expiration days as needed.
- **Simple Interface**: Easy-to-understand output for quick decision-making.

---

## How It Works
1. **Input Food Data**:
   - Food data is provided through a CSV file `data/sample_data.csv` or directly in the script.
2. **Safety Check**:
   - Evaluates each item's temperature and expiration days against predefined thresholds.
3. **Alert Generation**:
   - Flags items that are unsafe and provides specific reasons (e.g., "Temperature too high" or "Near expiration").

---

## File Structure
```plaintext
FoodMonitoringSystem/
├── data/
│   └── sample_data.csv       # Sample dataset for testing
├── docs/
│   └── README.md             # Documentation (this file)
└── src/
    └── main.py               # Main Python script for the system
```

---

## Setup 

### Prerequisites 
- Python 3.6 or higher installed on your system. 
- A text editor or IDE for reviewing and editing code. 

## Installation 
1. Clone the repository:
```bash 
git clone https://github.com/YourGitHubUsername/FoodMonitoringSystem.git
```
2. Navigate to the project directory: 
```bash 
cd FoodMonitoringSystem
```

---

## Usage 

### Using the Provided Sample Data 
1. Open the `src/main.py` script to review the code. 
2. Use the `data/sample_data.csv` file as the input dataset. 

### Running the Script 
Run the Python script from the terminal:
```bash 
python src/main.py
```

### Expected Output 
The script will display alerts for any food items that require attention. For example:
```plaintext
Food Monitoring System - Simple Version
========================================

Food Data:
- Milk: Temp=8°C, Expiration=3 days
- Meat: Temp=5°C, Expiration=1 days
- Vegetables: Temp=10°C, Expiration=5 days
- Fruits: Temp=6°C, Expiration=2 days

System Alerts:
ALERT: Milk exceeds safe temperature! (Temp: 8°C)
ALERT: Meat is near expiration! (Days left: 1)
ALERT: Vegetables exceeds safe temperature! (Temp: 10°C)
```

--- 

## Customization 

### Thresholds 
- Modify `ALERT_THRESHOLD` and `EXPIRATION_LIMIT` in `main.py` to customize temperature and expiration limits. 

### Input Data 
- Replace `sample_data.csv` with your own CSV file for real-world data. 

---

## Contributing 
Contributions are welcome! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request.

---

## Contact
For queries or contributions, contact:
 - [**GitHub**](https://github.com/DiyaSThange)



