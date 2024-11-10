import random
from datetime import datetime, timedelta
import pymongo

# Připojení k MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]
orders_collection = db["orders"]
returns_collection = db["returns"]

# Pomocná funkce pro generování náhodného data
def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

# Rozsah dat pro generování objednávek
start_date = datetime.now() - timedelta(days=730)  # Poslední 2 roky
end_date = datetime.now()

# Data pro generování
product_names = ["Laptop", "Smartphone", "Headphones", "TV", "Tablet", "Camera", "Printer", "Monitor"]
categories = ["Electronics", "Home Appliances", "Clothing", "Sports", "Books"]
regions = ["North America", "Europe", "Asia", "Australia", "South America"]
return_reasons = ["Defective", "Not as described", "Arrived late", "Changed mind"]

# Parametry
num_orders = 10000
return_probability = 0.1  # 10 % objednávek bude vráceno

# Generování dat
orders_data = []
returns_data = []

for i in range(num_orders):
    order_id = i + 1
    product_name = random.choice(product_names)
    category = random.choice(categories)
    price = round(random.uniform(5, 2000), 2)  # Cena mezi 5 a 2000
    quantity = random.randint(1, 5)
    order_date = random_date(start_date, end_date)
    customer_region = random.choice(regions)

    # Vytvoření záznamu objednávky
    order = {
        "order_id": order_id,
        "product_name": product_name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "order_date": order_date,
        "customer_region": customer_region,
    }
    orders_data.append(order)

    # Náhodné rozhodnutí, zda bude objednávka vrácena
    if random.random() < return_probability:
        return_date = order_date + timedelta(days=random.randint(1, 30))  # Datum vrácení do 30 dnů
        reason = random.choice(return_reasons)
        return_record = {
            "return_id": len(returns_data) + 1,
            "order_id": order_id,
            "return_date": return_date,
            "reason": reason,
        }
        returns_data.append(return_record)

# Vložení dat do MongoDB
orders_collection.insert_many(orders_data)
returns_collection.insert_many(returns_data)

# Uzavření připojení
client.close()

print(f"Inserted {len(orders_data)} orders and {len(returns_data)} returns into the database.")