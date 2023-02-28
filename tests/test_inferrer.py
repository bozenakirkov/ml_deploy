import os
import pytest

from poetrytest.inferrer import Inferrer


def test_infer_model_1():
    image = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "test_data/test_img_1000.npz")
    inferrer = Inferrer()
    inferrer.infer(image)


def test_infer_model_2():
    image = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "test_data/test_img_1000.npz")
    inferrer = Inferrer()
    inferrer.change_model("model_2")
    inferrer.infer(image)


def test_infer_file_not_found():
    image = "file not found"
    inferrer = Inferrer()
    with pytest.raises(FileNotFoundError):
        inferrer.infer(image)


def test_infer_empty_file():
    image = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "test_data/empty_file.txt")
    inferrer = Inferrer()
    with pytest.raises(ValueError):
        inferrer.infer(image)


