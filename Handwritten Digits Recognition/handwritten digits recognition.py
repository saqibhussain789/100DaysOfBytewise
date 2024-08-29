import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(loss= 'sparse_categorical_crossentropy', optimizer= 'Adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)


loss, accuracy = model.evaluate(x_test, y_test)

print(f"Loass: {loss}")
print(f"Accuracy: {accuracy}")

image_num = 1
while os.path.isfile(f"samples/digit{image_num}.png"):
    try:
        img = cv2.imread(f"samples/digit{image_num}.png")[:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f"This digit is: {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except:
        print("Error!")
    finally:
        image_num += 1
