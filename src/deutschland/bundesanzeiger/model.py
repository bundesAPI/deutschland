from pathlib import Path

import numpy as np
from onnxruntime import InferenceSession
from PIL import Image


class Model:
    def __init__(self):
        self.session = self.load_model()

    def load_model(self):
        filepath = Path(__file__).parent / "assets" / "model.onnx"
        return InferenceSession(str(filepath))

    @staticmethod
    def load_image_arr(fp):
        image = Image.open(fp).convert("L")
        image = np.array(image)
        image = image / 255 * 2
        image = image - 1
        return image

    @staticmethod
    def character_indexes_to_str(character_indexes):
        ALPHABET = list("abcdefghijklmnopqrstuvwxyz0123456789")
        characters = np.array(ALPHABET)[character_indexes]
        return "".join(list(characters)).upper()

    @staticmethod
    def prediction_to_str(label):
        character_indexes = np.argmax(label, axis=1)
        return Model.character_indexes_to_str(character_indexes)
