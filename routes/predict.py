from flask import Blueprint, jsonify, request

from services.risk_service import evaluate_risk

predict_bp = Blueprint("predict", __name__)


@predict_bp.post("/predict")
def predict():
    data = request.get_json()

    result = evaluate_risk(data)

    return jsonify(result)

