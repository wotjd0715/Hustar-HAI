import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from imgprocess import *

x_data = np.array(video_to_edgedFrame('200905.avi'))
y_data = np.array(pd.read_csv("result2.csv"))

#결과값 One Hot Encoding
ohen = OneHotEncoder()
ohen.fit(y_data)
y_data = ohen.transform(y_data).toarray()
y_data = np.argmax(y_data, axis = 1).reshape(-1,1)

#print(x_data.shape)
#print(y_data.shape)

#학습 데이터 나누기
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.2, random_state = 777)
print(x_train.shape)
print(y_train.shape)

#이미지 데이터 0~1 사이 데이터로 세팅
x_train, x_test = x_train/255.0, x_test/255.0

#학습 모델 제작
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(input_shape=(280,640,1), padding = "same", kernel_size=4, filters=20, strides=(2, 2)),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2,2)),
    tf.keras.layers.Conv2D(kernel_size=4,  filters=40, strides=(2,2)),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2,2)),
    tf.keras.layers.Conv2D(kernel_size=4, filters=80, strides=(2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(3, activation= 'softmax')
])

model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

#학습
model.fit(x_train.reshape(-1,280,640,1),y_train, epochs=5)

#평가
model.evaluate(x_test.reshape(-1,280,640,1),y_test)

model.save('model2/')