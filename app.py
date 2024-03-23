from flask import Flask, request, jsonify
import os
import sys
import json
from placement import make_prediction
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        input_data = request.json

        # Make prediction using the make_prediction function from placement.py
        prediction = make_prediction(input_data["Branch"], input_data["Gender"], input_data["tenth_percentage"], 
                                     input_data["twelfth_percentage"], input_data["CGPA_Till_sixth"], 
                                     input_data["sixth_Sem_SGPA"], input_data["Internship"], input_data["Skills"])
        
        
        
        if (prediction == 0):
            prediction='The person is not placed'
        else:
            prediction= 'The person is placed'
        # Return the prediction as a JSON response
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(port=os.getenv('server_port'))


    
    


