from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender import recommend

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/recommend", methods=["POST"])
def recommend_content():
    data = request.json

    results = recommend(
        age=data["age"],
        preferred_genres=data["genres"],
        content_type=data["type"]
    )

    return jsonify(results.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
