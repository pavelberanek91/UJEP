import os
import redis
import json
from pymongo import MongoClient
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Připojení k MongoDB
mongo_client = MongoClient(os.getenv("MONGO_URI"))
db = mongo_client["ecommerce"]
orders_collection = db["orders"]
returns_collection = db["returns"]

# Připojení k Redis
redis_client = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"))

# Funkce pro načítání a cachování dat
def get_cached_data(cache_key, pipeline, collection, expiration=3600):
    cached_data = redis_client.get(cache_key)
    if cached_data:
        return json.loads(cached_data)
    else:
        data = list(collection.aggregate(pipeline))
        redis_client.setex(cache_key, expiration, json.dumps(data))
        return data

# Funkce pro načítání různých metrik
def get_top_products():
    pipeline = [
        {"$group": {"_id": "$product_name", "total_quantity": {"$sum": "$quantity"}}},
        {"$sort": {"total_quantity": -1}},
        {"$limit": 5}
    ]
    return get_cached_data("top_products", pipeline, orders_collection)

def get_sales_by_region():
    pipeline = [
        {"$group": {
            "_id": {"region": "$customer_region", "month": {"$month": "$order_date"}},
            "total_sales": {"$sum": {"$multiply": ["$price", "$quantity"]}}
        }},
        {"$sort": {"_id.month": 1}}
    ]
    return get_cached_data("sales_by_region", pipeline, orders_collection)

def get_returns_by_category():
    pipeline = [
        {"$lookup": {
            "from": "returns",
            "localField": "order_id",
            "foreignField": "order_id",
            "as": "return_data"
        }},
        {"$unwind": "$return_data"},
        {"$group": {"_id": "$category", "return_count": {"$sum": 1}}}
    ]
    return get_cached_data("returns_by_category", pipeline, orders_collection)

def get_price_segments():
    pipeline = [
        {"$bucket": {
            "groupBy": "$price",
            "boundaries": [0, 50, 200, 1000, 5000],
            "default": "Other",
            "output": {"count": {"$sum": 1}}
        }}
    ]
    return get_cached_data("price_segments", pipeline, orders_collection)

# Vytvoření Dash aplikace
app = Dash(__name__)

# Layout aplikace
app.layout = html.Div([
    html.H1("E-commerce Dashboard"),
    
    # Top Products
    html.Div([
        html.H2("Top 5 Products"),
        dcc.Graph(id="top-products-chart")
    ]),

    # Sales by Region
    html.Div([
        html.H2("Sales by Region"),
        dcc.Graph(id="sales-by-region-chart")
    ]),

    # Returns by Category
    html.Div([
        html.H2("Returns by Category"),
        dcc.Graph(id="returns-by-category-chart")
    ]),

    # Price Segments
    html.Div([
        html.H2("Price Segments"),
        dcc.Graph(id="price-segments-chart")
    ])
])

# Callbacks pro aktualizaci grafů
@app.callback(
    Output("top-products-chart", "figure"),
    Input("top-products-chart", "id")
)
def update_top_products(_):
    data = get_top_products()
    df = pd.DataFrame(data)
    fig = px.bar(df, x="_id", y="total_quantity", title="Top 5 Products")
    return fig

@app.callback(
    Output("sales-by-region-chart", "figure"),
    Input("sales-by-region-chart", "id")
)
def update_sales_by_region(_):
    data = get_sales_by_region()
    df = pd.DataFrame(data)
    df["_id"] = df["_id"].apply(lambda x: f"{x['region']} - {x['month']}")
    fig = px.line(df, x="_id", y="total_sales", title="Sales by Region")
    return fig

@app.callback(
    Output("returns-by-category-chart", "figure"),
    Input("returns-by-category-chart", "id")
)
def update_returns_by_category(_):
    data = get_returns_by_category()
    df = pd.DataFrame(data)
    fig = px.pie(df, names="_id", values="return_count", title="Returns by Category")
    return fig

@app.callback(
    Output("price-segments-chart", "figure"),
    Input("price-segments-chart", "id")
)
def update_price_segments(_):
    data = get_price_segments()
    df = pd.DataFrame(data)
    fig = px.histogram(df, x="_id", y="count", title="Price Segments")
    return fig

# Spuštění serveru
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050)
