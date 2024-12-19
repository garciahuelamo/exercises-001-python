from flask import Flask, request, jsonify
import json
from pydantic import BaseModel, ValidationError

app = Flask(__name__)

class Item (BaseModel):
    title : str
    complete : bool

items = []

@app.route('/api/todolist', methods=['POST'])
def get_item():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "missing data"})
    new_item = {
        "id" : len(items) + 1,
        "title" : data['title'],
        "complete" : data['complete']
    }

    items.append(new_item)

    return jsonify({"message" : "Item saved","item" : new_item})

if __name__ == "__main__":
    app.run(debug=True)