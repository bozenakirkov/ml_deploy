from poetrytest.inferrer import Inferrer
import os


def test_infer():
    image = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "test_data/test_img_1000.npz")
    inferrer = Inferrer()
    inferrer.infer(image)

