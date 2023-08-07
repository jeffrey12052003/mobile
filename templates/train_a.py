import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import accuracy_score
from scipy.sparse import csr_matrix
import numpy as np
import pickle
def used_price_prediction(input_features):
    df = pd.read_csv('processed_data.csv')
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model.predict([input_features])
def convert_to_original_price(converted_price):
    original_min = 2.901422
    original_max = 7.847841
    new_min = 500
    new_max = 50000

    original_price = (converted_price - new_min) / (new_max - new_min) * (original_max - original_min) + original_min
    return original_price
def convert_price(original_price):
    original_min = 2.901422
    original_max = 7.847841
    new_min = 500
    new_max = 50000

    converted_price = (original_price - original_min) / (original_max - original_min) * (new_max - new_min) + new_min
    return converted_price

def success_rate(days_used,predicted_resale_price,market_price):
    if days_used <= 100:
        if predicted_resale_price >= 0.85 * market_price:
            return True
    elif days_used <= 200:
        if predicted_resale_price >= 0.75 * market_price:
            return True
    elif days_used <= 300:
        if predicted_resale_price >= 0.60 * market_price:
            return True
    elif days_used <= 400:
        if predicted_resale_price >= 0.52 * market_price:
            return True
    elif days_used <= 500:
        if predicted_resale_price >= 0.45 * market_price:
            return True
    elif days_used <= 600:
        if predicted_resale_price >= 0.35 * market_price:
            return True
    elif days_used <= 800:
        if predicted_resale_price >= 0.25 * market_price:
            return True
    elif days_used <= 1100:
        if predicted_resale_price >= 0.20 * market_price:
            return True
    else:
        if days_used > 1100:
            if predicted_resale_price > 18 * market_price:
                return True
            else:
                return False

    return False


