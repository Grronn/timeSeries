import os
import random
import pandas as pd

def generate_temperature_data(start_date, end_date, anomalies_probability, noise_level):
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    temperature_data = []

    for date in date_range:
        temperature = random.uniform(15, 30)

        if random.uniform(0, 1) < anomalies_probability:
            temperature += random.uniform(-5, 5)

        temperature += random.uniform(-noise_level, noise_level)

        temperature = round(temperature)

        temperature_data.append({'date': date, 'temperature': temperature})

    return temperature_data

def save_data_to_file(data, folder, filename):
    file_path = os.path.join(folder, filename)
    data_frame = pd.DataFrame(data)
    data_frame.to_csv(file_path, index=False)

datasets_parameters = [
    {'start_date': '2024-01-01', 'end_date': '2024-06-30', 'anomalies_probability': 0.1, 'noise_level': 2},
    {'start_date': '2024-07-01', 'end_date': '2024-12-31', 'anomalies_probability': 0.15, 'noise_level': 3},
    {'start_date': '2025-01-01', 'end_date': '2025-06-30', 'anomalies_probability': 0.2, 'noise_level': 2.5}
]

for i, params in enumerate(datasets_parameters, start=1):
    train_data = generate_temperature_data(**params)
    test_data = generate_temperature_data(**params)


    os.makedirs('train', exist_ok=True)
    os.makedirs('test', exist_ok=True)

    save_data_to_file(train_data, 'train', f'train_data_set_{i}.csv')
    save_data_to_file(test_data, 'test', f'test_data_set_{i}.csv')
