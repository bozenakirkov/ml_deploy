from flask import Flask, request
from poetrytest.inferrer import Inferrer
from flasgger import Swagger
import os

app = Flask(__name__)
swagger = Swagger(app)

upload_folder = "../tmp"
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)
app.config['uploadFolder'] = upload_folder

inferrer = Inferrer()


@app.route("/infer", methods=["POST"])
def infer():
    """Predict digits
        ---
        parameters:
        - name: input_file
          in: formData
          type: file
          required: true
          description: Select NPZ file with tensor data.
        responses:
          default:
            description: Predictions for [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] digits.
        """
    input_file = request.files.get("input_file")
    input_file_path = os.path.join(app.config['uploadFolder'],
                                   input_file.filename)
    input_file.save(input_file_path)
    return inferrer.infer(input_file_path)


if __name__ == '__main__':
    app.run()

