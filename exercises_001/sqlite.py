from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "productos.db"

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL NOT NULL)
            """
        )

init_db()

#CREATE

@app.route("/api/products", methods=['POST'])
def create_products():
    data = request.json
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute(
            "INSERT INTO products(name, price) VALUES (?,?)", (data["name"], data["price"])
        )

        conn.commit() #Para enviar el prompt solicitado

    return jsonify({"id": cursor.lastrowid}), 201

#LIST

@app.route("/api/products", methods=['GET'])
def list_products():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute(
            "SELECT * FROM products"
        )

        products = [
            {"id" : row[0], "name" : row[1], "price" : row[2]}

            for row in cursor.fetchall() #Iterar todas las líneas que haya en el cursor y crear una lista de objetos
        ]

    return jsonify({"message" : "Lista leída con éxito"})

#UPDATE

@app.route("/api/products/<int:id>", methods=['PUT'])
def update_products(id):
    data = request.json
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute(
            "UPDATE products SET name=?, price=? WHERE id=?", (data["name"], data["price"], id)
        )
    
    conn.commit()

    return jsonify({"message": "Producto actualizado"})

#DELETE

@app.route("/api/products/<int:id>", methods=['DELETE'])
def delete_products(id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute(
            "DELETE FROM products WHERE id=?", (id,)
        )
    
    conn.commit()
    
    return jsonify({"message": "Producto eliminado"})

if __name__ == "__main__":
    app.run(debug=True)