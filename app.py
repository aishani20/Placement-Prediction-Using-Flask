from flask import Flask, request, jsonify
import os
import sys
import json
from placement import make_prediction
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)

# cors is cross origin resource sharing, flask-cors is used to allow the frontend to access the backend
CORS(app, origins=os.getenv("CORS_ORIGIN"), supports_credentials=True)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data from the request
        input_data = request.json

        # Make prediction using the make_prediction function from placement.py
        prediction = make_prediction(
            input_data["Branch"],
            input_data["Gender"],
            input_data["tenth_percentage"],
            input_data["twelfth_percentage"],
            input_data["CGPA_Till_sixth"],
            input_data["sixth_Sem_SGPA"],
            input_data["Internship"],
            input_data["Skills"],
        )

        if prediction == 0:
            prediction = "You have low chances of getting placed."
        elif prediction == 1:
            prediction = "The person has high chances of getting placed."
        else:
            prediction = "Error in prediction. Please contact the developer."

        # Return the prediction as a JSON response
        return jsonify(
            {
                "success": True,
                "message": "Prediction Done Successfully",
                "result": prediction,
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/home", methods=["GET"])
def home():
    response = jsonify({"message": "Welcome to Placement Prediction Web App"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    print("Starting Flask API", os.getenv("server_port"))
    app.run(host="0.0.0.0", port=os.getenv("server_port"))
