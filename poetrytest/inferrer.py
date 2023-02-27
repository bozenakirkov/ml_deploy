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
        self.saved_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                       "../model_2"))
        self.model_version = os.path.basename(self.saved_path)
        self.model = tf.saved_model.load(self.saved_path)
        self.predict = self.model.signatures["serving_default"]

    @staticmethod
    def preprocess(image_npz: str) -> Tuple[tf.Tensor, np.array]:
        if not os.path.exists(image_npz):
            raise FileNotFoundError
        image = np.load(image_npz)
        return tf.expand_dims(image["inputs"], axis=0), image["targets"]

    def infer(self, img_path_npz: str) -> str:
        image, target = self.preprocess(img_path_npz)
        prediction = self.predict(image)
        output_key = self.mapping[self.model_version]["out"]
        result = "Ground truth: " + str(target) + \
                 "\nPredicted values for [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: \n" \
                 + str(prediction[output_key])
        return result

