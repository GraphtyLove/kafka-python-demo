from requests import Session

with Session as sess:
    for i in range(1000):
        data = {
            "id": i,
            "store": "Brussels",
            "date": "2020-01-01",
            "products": [
                {
                    "id": "123456789",
                    "name": "Banana",
                    "price": 1.5
                },
                {
                    "id": "123456789",
                    "name": "Bread",
                    "price": 1.5
                },
                {
                    "id": "123456789",
                    "name": "Water",
                    "price": 1.5
                }
            ]
        }
        sess.post("http://localhost:8000/data", json=data)