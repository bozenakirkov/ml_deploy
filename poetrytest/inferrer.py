import tensorflow as tf
import numpy as np
import os
import glob


class Inferrer:
    def __init__(self):
        self.saved_path = glob.glob('../mymodel')[0]
        self.model = tf.saved_model.load(self.saved_path)
        self.predict = self.model.signatures["serving_default"]

    @staticmethod
    def preprocess(image_npz):
        if not os.path.exists(image_npz):
            image_npz = '../tests/test_data/test_image_1000.npz'
        image = np.load(image_npz)
        return tf.expand_dims(image["arr_0"], axis=0)

    def infer(self, img_path_npz):
        image = self.preprocess(img_path_npz)
        try:
            prediction = self.predict(input_1=image)
        except Exception:
            raise

        return "All predicted values: " + str(prediction["output_1"])


