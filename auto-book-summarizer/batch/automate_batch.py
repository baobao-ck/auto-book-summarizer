
import requests

def automate_workflow(book_path):
    with open(book_path, 'rb') as f:
        upload = requests.post("http://<load-balancer>/upload", files={"file": f})
    print(upload.json())

    requests.post("http://<load-balancer>/summarize", json={"s3_key": "uploaded-book.pdf"})
    requests.post("http://<load-balancer>/generate-tts", json={"summary_id": "summary-xyz"})
    requests.post("http://<load-balancer>/generate-video", json={"tts_id": "tts-xyz"})
