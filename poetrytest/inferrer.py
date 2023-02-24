import tensorflow as tf
import numpy as np
import os
import glob


class Inferrer:
    def __init__(self):
        self.saved_path = glob.glob('../mymodel')[0]
        print(os.getcwd())
        self.model = tf.saved_model.load(self.saved_path)
        self.predict = self.model.signatures["serving_default"]

    def preprocess(self, image):
        if not image:
            image = np.load('../tests/test_data/test_image_0.npz')
        return tf.expand_dims(image["arr_0"], axis=0)

    def infer(self, image=None):
        image = self.preprocess(image)
        prediction = self.predict(input_1=image)

        return str(prediction["output_1"])
