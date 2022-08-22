import os

import numpy as np
import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import cv2

def predict(data, weight):
    model = keras.models.load_model(weight)

    categories = ["CPU", "GPU", "RAM"]

    size = (150, 150)

    test_ds = os.listdir(data)

    img = cv2.imread(data+test_ds[0])
    img = cv2.resize(img, dsize=size)

    predictions = model.predict(np.expand_dims(img, axis=0))
    predictions = list(map(np.argmax, predictions))

    print(f"Predicted as {categories[predictions[0]]}")
    return categories[predictions[0]]