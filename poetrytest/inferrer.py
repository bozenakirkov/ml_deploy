import os
from typing import Tuple

import tensorflow as tf
import numpy as np


class Inferrer:
    def __init__(self):
        self.mapping = {
            "model_1":
                {"in": "inputs", "out": "output_1"},
            "model_2":
                {"in": "flatten_input", "out": "last_layer"}
        }
        self.model_version = "model_1"  # default
        self.saved_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                       "../" + self.model_version))
        self.predict = tf.saved_model.load(self.saved_path).signatures["serving_default"]

    @staticmethod
    def preprocess(image_npz: str) -> Tuple[tf.Tensor, np.array]:
        if not os.path.exists(image_npz):
            raise FileNotFoundError
        try:
            image = np.load(image_npz)
        except ValueError as ex:
            raise
        return tf.expand_dims(image["inputs"], axis=0), image["targets"]

    def change_model(self, model):
        if model != self.model_version:
            self.model_version = model
            self.saved_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "../"
                             + self.model_version))
            self.predict = tf.saved_model.load(
                self.saved_path).signatures["serving_default"]

    def infer(self, img_path_npz: str) -> str:
        image, target = self.preprocess(img_path_npz)
        prediction = self.predict(image)
        output_key = self.mapping[self.model_version]["out"]
        result = "Ground truth: " + str(target) + \
                 "\nPredicted values for [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: \n" \
                 + str(prediction[output_key])
        return result

