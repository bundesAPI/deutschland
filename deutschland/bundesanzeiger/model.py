from tensorflow import keras

import tensorflow.keras.backend as K

import numpy as np
from PIL import Image


def load_image_arr(fp):
    image = Image.open(fp).convert("L")
    image = np.array(image)
    image = image / 255 * 2
    image = image - 1
    return image


def character_indexes_to_str(character_indexes):
    ALPHABET = list("abcdefghijklmnopqrstuvwxyz0123456789")
    characters = np.array(ALPHABET)[character_indexes]
    return "".join(list(characters)).upper()


def prediction_to_str(label):
    character_indexes = np.argmax(label, axis=1)
    return character_indexes_to_str(character_indexes)


def my_accuracy(y_true, y_pred):
    return K.cast(
        K.all(K.equal(K.argmax(y_true, axis=2), K.argmax(y_pred, axis=2)), axis=1),
        K.floatx(),
    )


def load_model():
    return keras.models.load_model(
        "assets/model.h5", custom_objects={"my_accuracy": my_accuracy}
    )
