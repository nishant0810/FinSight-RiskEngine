def calculate_debt_ratio_risk(income, loan_amount):
    ratio = loan_amount / max(income, 1)

    if ratio >= 2.0:
        return 0.50, "Extremely high debt-to-income ratio"

    if ratio >= 1.5:
        return 0.35, "High debt-to-income ratio"

    if ratio >= 1.0:
        return 0.15, "Moderately elevated debt-to-income ratio"

    return 0.0, None


def calculate_credit_risk(score):
    if score < 550:
        return 0.40, "Very poor credit score"

    if score < 650:
        return 0.25, "Credit score below preferred threshold"

    if score < 700:
        return 0.10, "Fair credit score"

    return 0.0, None


def calculate_existing_loan_risk(existing):
    if existing >= 5:
        return 0.30, "Excessive number of active loans"

    if existing >= 3:
        return 0.20, "Multiple existing loans"

    if existing == 2:
        return 0.05, "Several active loans"

    return 0.0, None