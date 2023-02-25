import requests
ENDPOINT_URL = "http://127.0.0.1:5000/infer"


def infer():
    response = requests.post(ENDPOINT_URL, json={"input_file": '../tests/test_data'})
    response.raise_for_status()
    print(response.text)


if __name__ =="__main__":
    infer()
