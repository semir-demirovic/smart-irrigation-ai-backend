import random

def get_moisture_data():
    """Simulates a physical soil moisture hardware sensor reading (20% to 80%)"""
    # This replaces the need for a CSV file and acts as a virtual IoT device
    return random.randint(20, 80)