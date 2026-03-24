import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt

# Пути к папкам
train_data_dir = 'processed_dataset'  # твоя обработанная папка с изображениями
img_height, img_width = 224, 224
batch_size = 8

# Генератор данных для обучения
datagen = ImageDataGenerator(
    validation_split=0.2, # 80% train, 20% validation
    rescale=1./255,
    rotation_range=20,
    horizontal_flip=True,
)

train_gen = datagen.flow_from_directory(
    'processed_dataset', # твоя папка с обработанными изображениями
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

val_gen = datagen.flow_from_directory(
    'processed_dataset',
    subset='validation',
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical'
)

# Создание и компиляция модели
model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

model.trainable = False  # заморозим веса

# Добавим верхние слои
x = tf.keras.layers.GlobalAveragePooling2D()(model.output)
x = tf.keras.layers.Dense(128, activation='relu')(x)
output = tf.keras.layers.Dense(len(train_gen.class_indices), activation='softmax')(x)

model = tf.keras.Model(inputs=model.input, outputs=output)

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Обучение модели
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=10
)

# Сохраняем модель
model.save("clothing_classifier.keras")

# Визуализация результатов обучения
import matplotlib.pyplot as plt

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
epochs = range(len(acc))

plt.plot(history.history['accuracy'], label='Точность на обучении')
plt.plot(history.history['val_accuracy'], label='Точность на валидации')
plt.xlabel('Эпоха')
plt.ylabel('Точность')
plt.legend()
plt.show()
