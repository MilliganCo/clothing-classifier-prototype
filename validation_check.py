import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Загрузи обученную модель
model = tf.keras.models.load_model('clothing_classifier.keras')

# Правильный путь к изображению (добавлен префикс r)
img_path = r'D:\PyCharm 2024.2.3\PycharmProjects\clothing_class\w070225_133963 copy.jpg'

# Подготовка изображения
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Предсказание
predictions = model.predict(img_array)
predicted_class = np.argmax(predictions, axis=1)[0]

# Укажи названия категорий в точности как у тебя в папке processed_dataset
labels = ['dress', 'hoodie', 'skirt', 'sport_suit', 'towel', 'tshirt']

print(f"Предсказанный класс: {labels[predicted_class]}")
