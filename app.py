from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

UPLOAD_FOLDER = "uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route('/insert', methods=['POST'])
def insert_product():
    category = request.form.get("category")
    name = request.form.get("name")
    price = request.form.get("price")
    image = request.files.get("image")

    if image:
        image_path = UPLOAD_FOLDER + image.filename
        image.save(image_path)
    else:
        return jsonify({"message": "Image upload failed"}), 400

    data = {
        "category": category,
        "name": name,
        "price": price,
        "image": image.filename
    }

    response = requests.post("http://127.0.0.1/insert.php", data=data)

    return response.json()


if __name__ == '__main__':
    app.run(debug=True)
