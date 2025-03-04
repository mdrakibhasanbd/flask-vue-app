from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

app = Flask(__name__)
CORS(app)

def get_mongo_db():
    try:
        load_dotenv()
        mongoDatabase = os.getenv("MONGO_DB_NAME")
        mongo_replica = os.getenv("MONGO_REPLICA_URI")
        mongo_client = MongoClient(mongo_replica)
        db = mongo_client.get_database(mongoDatabase)
        return mongo_client, db
    except ServerSelectionTimeoutError as e:
        print(f"Server selection timeout error: {e}")
        # Handle the error (e.g., log, retry, return a default value)
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        # Handle the error as needed (e.g., log, raise, return a default value)
        return None
# MongoDB Configuration
mongo_client, db = get_mongo_db()

if mongo_client is None:
    print("Failed to connect to the database. Exiting...")
    exit(1)

client, database = get_mongo_db()
item_collection = database.get_collection("items")

@app.route('/api/v1/test', methods=['GET'])
def test_api():
    return jsonify({"message": "Hello from Flask API!", "status": "success"})

# Create (Insert Data)
@app.route("/api/v1/add-item", methods=["POST"])
def create_item():
    data = request.json
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid input"}), 400

    item_id = item_collection.insert_one({"name": data["name"], "price": data["price"]}).inserted_id
    return jsonify({"message": "Item created", "id": str(item_id)}), 201


# Read (Get All Data)
@app.route("/api/v1/get-items", methods=["GET"])
def get_items():
    items = []
    for item in item_collection.find():
        items.append({"id": str(item["_id"]), "name": item["name"], "price": item["price"]})
    return jsonify(items), 200


# Read (Get Single Data by ID)
@app.route("/api/v1/get-item-by-id/<_id>", methods=["GET"])
def get_item(_id):
    item = item_collection.find_one({"_id": ObjectId(_id)})
    if item:
        return jsonify({"id": str(item["_id"]), "name": item["name"], "price": item["price"]}), 200
    return jsonify({"error": "Item not found"}), 404


# Update (Modify Data)
@app.route("/api/v1/update-item/<_id>", methods=["PUT"])
def update_item(_id):
    data = request.json
    updated_item = item_collection.find_one_and_update(
        {"_id": ObjectId(_id)},
        {"$set": {"name": data.get("name"), "price": data.get("price")}},
        return_document=True,
    )
    if updated_item:
        return jsonify({"message": "Item updated"}), 200
    return jsonify({"error": "Item not found"}), 404


# Delete (Remove Data)
@app.route("/api/v1/delete-item/<_id>", methods=["DELETE"])
def delete_item(_id):
    result = item_collection.delete_one({"_id": ObjectId(_id)})
    if result.deleted_count:
        return jsonify({"message": "Item deleted"}), 200
    return jsonify({"error": "Item not found"}), 404


# Run the App
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

