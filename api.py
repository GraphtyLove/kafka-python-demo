from fastapi import FastAPI
from kafka import KafkaProducer
from json import dumps



app = FastAPI()

# Initiate Producer with Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    # Encode the data to bytes (required by Kafka)
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

print("Producer Ready!")


@app.post("/data")
def data(data: dict):
    # Send the message to the queue    
    producer.send('delhaize_shop', data)
    
    print("sent to queue!")
    return {"status": "ok"}

