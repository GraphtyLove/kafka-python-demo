# Python with Kafka

Small example of how to use Kafka with Python.

## Requirements
- Python 3.10
- Docker
- Docker Compose
- Install python dependencies with `pip install -r requirements.txt`

## Run
- Start Kafka with `docker-compose up -d`
- Run the consumer with `python consumer.py`
- Run the API with `uvicorn api:app --reload`
- Send a message with the API, you can see the doc at: `http://localhost:8000/docs`
- Test the system with `python test.py`