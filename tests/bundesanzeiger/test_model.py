from pathlib import Path

import numpy as np
from onnxruntime import InferenceSession

from deutschland.bundesanzeiger.model import (
    load_image_arr,
    load_model,
    prediction_to_str,
)


def test_load_model():
    assert isinstance(load_model(), InferenceSession)


def test_prediction():
    # load the model
    model = load_model()

    # load the captcha image
    filepath = Path(__file__).parent / "captcha.png"
    image_arr = load_image_arr(filepath).reshape((1, 50, 250, 1))

    # predict
    prediction = model.run(None, {"captcha": image_arr.astype(np.float32)})[0][0]

    # translate prediction to captcha solution
    assert prediction_to_str(prediction) == "KCDKTM"
