from pathlib import Path

import numpy as np
from onnxruntime import InferenceSession

from deutschland.bundesanzeiger.model import Model


def test_load_model():
    assert isinstance(Model().session, InferenceSession)


def test_prediction():
    # load the model
    model = Model().load_model()

    # load the captcha image
    filepath = Path(__file__).parent / "captcha.png"
    image_arr = Model.load_image_arr(filepath).reshape((1, 50, 250, 1))

    # predict
    prediction = model.run(None, {"captcha": image_arr.astype(np.float32)})[0][0]

    # translate prediction to captcha solution
    assert Model.prediction_to_str(prediction) == "KCDKTM"
