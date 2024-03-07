import os
import numpy as np
import pandas as pd

# Создаем папки "train" и "test", если они еще не существуют
os.makedirs("train", exist_ok=True)
os.makedirs("test", exist_ok=True)

# Генерируем данные для тренировочного набора
np.random.seed(0)
dates_train = pd.date_range(start='1/1/2021', periods=100)
temperatures_train = round(np.random.normal(20, 5, 100))
temperatures_train[20:25] += 10  # Добавляем аномалии
temperatures_train += np.random.normal(0, 2, 100)  # Добавляем шум

df_train = pd.DataFrame({'Date': dates_train, 'Temperature': temperatures_train})
df_train.to_csv('train/temperature_data_train.csv', index=False)

# Генерируем данные для тестового набора
dates_test = pd.date_range(start='4/11/2021', periods=50)
temperatures_test = round(np.random.normal(18, 4, 50))
temperatures_test[10:15] += 8  # Добавляем аномалии
temperatures_test += np.random.normal(0, 1.5, 50)  # Добавляем шум

df_test = pd.DataFrame({'Date': dates_test, 'Temperature': temperatures_test})
df_test.to_csv('test/temperature_data_test.csv', index=False)
