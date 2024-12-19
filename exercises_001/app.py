from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api/wellcome', methods=['GET'])
def func_wellcome():
    return jsonify({"message": "Wellcome to our API!"})

if __name__ == '__main__':
    app.run(debug=True)