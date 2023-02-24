from poetrytest.inferrer import Inferrer


def test_infer():
    image = "../test_data/test_image_1000.npz"
    inferrer = Inferrer()
    inferrer.infer(image)

