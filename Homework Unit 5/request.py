import requests


url="http://localhost:9696/predict"

customer = {"job": "retired", "duration": 445, "poutcome": "success"}

customer2 = {"job": "unknown", "duration": 270, "poutcome": "failure"}

response = requests.post(url, json=customer).json()
print(response)
if response["score"]:
    print("send email, prob ", response["score_prob"] )
else:
    print("do not send email, prob ", response["score_prob"] )
