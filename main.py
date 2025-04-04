from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

expenses = [ 
    
  {"month": "January", "amount": 1200},
    {"month": "February", "amount": 1300},
    {"month": "March", "amount": 1100},
    {"month": "April", "amount": 1250},
    {"month": "May", "amount": 1400}

]

@app.route('/api/expenses',methods = ['GET'])
def get_expenses():
    """Fatch past expenses"""
    return jsonify(expenses)

@app.route('/api/predict',methods = ['GET'])
def predict_expense():
    """predict next month's expenses(simple avg)"""
    avg_expense = sum([e["amount"]for e in expenses])/len(expenses)
    return jsonify({"next_month_expens":round(avg_expense,2)})

@app.route('/api/savings-advice',methods = ['POST'])
def savings_advice():
    """suggesst saving strategy based on income """
    request_data = request.json
    income = request_data.get("income")

    avg_expense = sum([e["amount"]for e in expenses])/len(expenses)
    if income > avg_expense*1.5:
        advice = "You're saving well! Consider investing"
    elif income >avg_expense:
        advice = "You're managing well. Try reducing unnecessary expenses."
    else:
        advice = "Your expenses are higher than income! Cut down on luxury spending."

    return jsonify({"advice":advice})

if __name__ == '__main__':
    app.run(debug=True)