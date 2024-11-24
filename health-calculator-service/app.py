from flask import Flask, request, jsonify, render_template
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bmi', methods=['POST'])
def bmi():
    try:
        data = request.json
        height = data['height']
        weight = data['weight']
        if height <= 0 or weight <= 0:
            return jsonify({"error": "Height and weight must be positive numbers"}), 400
        result = calculate_bmi(height, weight)
        return jsonify({"bmi": result})
    except KeyError as e:
        return jsonify({"error": f"Missing key: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/bmr', methods=['POST'])
def bmr():
    try:
        data = request.json
        height = data['height']
        weight = data['weight']
        age = data['age']
        gender = data['gender']
        if height <= 0 or weight <= 0 or age <= 0:
            return jsonify({"error": "Height, weight, and age must be positive numbers"}), 400
        result = calculate_bmr(height, weight, age, gender)
        return jsonify({"bmr": result})
    except KeyError as e:
        return jsonify({"error": f"Missing key: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
