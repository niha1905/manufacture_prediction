import pandas as pd
import numpy as np
from datetime import timedelta, datetime
import random

num_samples = 10000

items = ['Apple', 'Banana', 'Tomato', 'Potato', 'Onion', 'Garlic', 'Ginger', 'Cucumber', 'Carrot',
         'Broccoli', 'Spinach', 'Lettuce', 'Cabbage', 'Cauliflower', 'Brinjal', 'Pumpkin', 'Bottle Gourd', 
         'Ridge Gourd', 'Bitter Gourd', 'Cluster Beans', 'French Beans', 'Drumstick', 'Snake Gourd', 
         'Ivy Gourd', 'Taro Root', 'Sweet Potato', 'Radish', 'Beetroot', 'Okra', 'Capsicum', 'Green Chili', 
         'Coriander Leaves', 'Mint Leaves', 'Fenugreek Leaves', 'Spring Onion', 'Amaranth Leaves', 'Ash Gourd', 
         'Pointed Gourd', 'Turnip', 'Jackfruit', 'Mango', 'Papaya', 'Pomegranate', 'Pear', 'Grapes', 
         'Lemon', 'Orange', 'Pineapple', 'Chikoo', 'Guava']

spoilage_time = {
    'Apple': 30, 'Banana': 7, 'Tomato': 10, 'Potato': 60, 'Onion': 30, 'Garlic': 90, 'Ginger': 20, 'Cucumber': 14, 
    'Carrot': 21, 'Broccoli': 10, 'Spinach': 4, 'Lettuce': 5, 'Cabbage': 21, 'Cauliflower': 14, 'Brinjal': 7,
    'Pumpkin': 20, 'Bottle Gourd': 14, 'Ridge Gourd': 10, 'Bitter Gourd': 7, 'Cluster Beans': 7, 'French Beans': 7,
    'Drumstick': 10, 'Snake Gourd': 14, 'Ivy Gourd': 14, 'Taro Root': 30, 'Sweet Potato': 45, 'Radish': 10, 
    'Beetroot': 30, 'Okra': 7, 'Capsicum': 10, 'Green Chili': 10, 'Coriander Leaves': 3, 'Mint Leaves': 3, 
    'Fenugreek Leaves': 3, 'Spring Onion': 5, 'Amaranth Leaves': 3, 'Ash Gourd': 30, 'Pointed Gourd': 14, 
    'Turnip': 21, 'Jackfruit': 7, 'Mango': 6, 'Papaya': 7, 'Pomegranate': 30, 'Pear': 10, 'Grapes': 14, 
    'Lemon': 30, 'Orange': 30, 'Pineapple': 14, 'Chikoo': 7, 'Guava': 10
}

def calculate_spoilage(type, temp, humidity):
    base_days = spoilage_time[type]
    temp_adjustment = (4 - temp) * 1.5
    if humidity > 70:
        humidity_adjustment = -(humidity - 70) * 0.2
    else:
        humidity_adjustment = 0
    return max(1, int(base_days + temp_adjustment + humidity_adjustment))

data = {
    "Date_of_Purchase": [datetime(2024, 1, 1) + timedelta(days=i%365) for i in range(num_samples)],
    "Type": random.choices(items, k=num_samples),
    "Fridge_Temperature_C": np.random.uniform(2, 8, num_samples),
    "Humidity_Percentage": np.random.uniform(50, 90, num_samples),
}

data['Spoilage_Days'] = [calculate_spoilage(item, temp, humidity) for item, temp, humidity in zip(data['Type'], data['Fridge_Temperature_C'], data['Humidity_Percentage'])]

large_spoilage_df = pd.DataFrame(data)
large_spoilage_df.to_csv('large_indian_spoilage_dataset.csv', index=False)
