from utils.scoring import (
    calculate_debt_ratio_risk,
    calculate_credit_risk,
    calculate_existing_loan_risk,
)


def evaluate_risk(data: dict) -> dict:
    income = float(data["income"])
    loan_amount = float(data["loanAmount"])
    credit_score = int(data["creditScore"])
    existing_loans = int(data["existingLoans"])

    risk = 0.0
    reasons = []

    debt_risk, debt_reason = calculate_debt_ratio_risk(
        income,
        loan_amount,
    )
    risk += debt_risk
    if debt_reason:
        reasons.append(debt_reason)

    credit_risk, credit_reason = calculate_credit_risk(
        credit_score,
    )
    risk += credit_risk
    if credit_reason:
        reasons.append(credit_reason)

    existing_risk, existing_reason = calculate_existing_loan_risk(
        existing_loans,
    )
    risk += existing_risk
    if existing_reason:
        reasons.append(existing_reason)

    risk = min(risk, 1.0)

    approval_probability = round(1 - risk, 2)
    confidence = 0.92

    if risk < 0.30:
        decision = "APPROVED"

        if not reasons:
            reasons.extend([
                "Strong repayment profile",
                "Healthy credit characteristics",
            ])

    elif risk < 0.70:
        decision = "MANUAL_REVIEW"
    else:
        decision = "REJECTED"

    return {
        "riskScore": round(risk, 2),
        "approvalProbability": approval_probability,
        "confidence": confidence,
        "decision": decision,
        "reasons": reasons,
    }