from flask import Flask, request
from poetrytest.inferrer import Inferrer
import os

# APP_ROOT = os.getenv('APP_ROOT', '/infer')

app = Flask(__name__)

inferrer = Inferrer()


@app.route("/infer", methods=["POST"])
def infer():
    data = request.json
    img_path_npz = data.get("input_file")
    return inferrer.infer(img_path_npz)


if __name__ == '__main__':
    # host = HOST, port = PORT_NUMBER
    app.run()
