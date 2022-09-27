from kafka import KafkaConsumer
from json import loads, dumps
from time import sleep

categories_mapper = {
    "Fruit": ["apple", "banana", "orange", "pear", "kiwi"],
    "Bakery": ["bread", "croissant", "baguette", "cake"],
    "Drink": ["water", "soda", "beer", "wine"],
}

# Initiate Consumer with Kafka
consumer = KafkaConsumer(
    'delhaize_shop',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    # Decode the data from bytes (required by Kafka)
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

# Read messages from the queue
for message in consumer:
    # Get the data from the message
    message_data = message.value
    # Compute the total price
    total_price = 0
    # Loop over the products
    for product in message_data["products"]:
        # Lower the product name to fit the categories_mapper
        product_name = product["name"].lower()
        # If the product is in the categories_mapper, add the corresponding category
        for category, values in categories_mapper.items():
            if product_name in values:
                product["category"] = category
        # If not, add it to the "Other" category
        else:
            product["category"] = "Other"
        # Compute the total price
        total_price += product["price"]
    
    print("Processed data: ", message_data)
    # Read the DB
    with open("database.json", "r") as file:
        file_content = file.read()
        #  If there is no content, add the first element in a list
        if not file_content:
            file_content = [message_data]
        # Else, append the element to the DB
        else:
            file_content = loads(file_content)
            file_content.append(message_data)
    # Write the processed element to the DB
    with open("database.json", "w") as file:
        file.write(dumps(file_content))
    # Wait 1sec to avoid overloading the CPU
    sleep(1)
