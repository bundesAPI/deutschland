from pathlib import Path

import numpy as np
from onnxruntime import InferenceSession
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


def load_model():
    filepath = Path(__file__).parent / "assets" / "model.onnx"
    return InferenceSession(str(filepath))
