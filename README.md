# 🤖 FinSight AI – Risk Engine

> AI-powered loan risk assessment microservice built with Flask.

The **Risk Engine** is an independent microservice responsible for evaluating loan applications and generating intelligent underwriting decisions. It receives applicant financial data from the Spring Boot backend, calculates multiple risk metrics, and returns an explainable decision along with supporting reasons.

The service is designed to be modular so that the current rule-based engine can be replaced with a machine learning model in the future without changing the backend API.

---

# 🚀 Features

- 📊 Loan Risk Assessment
- 💳 Credit Score Evaluation
- 💰 Debt-to-Income Ratio Analysis
- 🏦 Existing Loan Analysis
- 📈 Approval Probability Prediction
- 🤖 Explainable AI Responses
- 🔗 REST API Integration
- 🧩 Modular Architecture
- ⚡ Lightweight Flask Microservice

---

# 🏗️ System Architecture

```
                    +----------------------+
                    |    React Frontend    |
                    +----------+-----------+
                               |
                               |
                        REST API Calls
                               |
                               ▼
                  +-------------------------+
                  | Spring Boot Backend API |
                  +------------+------------+
                               |
                     HTTP REST Communication
                               |
                               ▼
                  +-------------------------+
                  |    Flask Risk Engine    |
                  +------------+------------+
                               |
                     Risk Evaluation Logic
                               |
                               ▼
                      JSON Risk Response
```

---

# 📂 Project Structure

```
risk-engine
│
├── app.py                  # Application entry point
│
├── routes
│   └── predict.py          # Prediction API
│
├── services
│   └── risk_service.py     # Risk evaluation logic
│
├── requirements.txt
│
└── README.md
```

---

# 🧠 Risk Evaluation Pipeline

The current engine uses explainable heuristic rules.

### 1. Debt-to-Income Ratio

```
Loan Amount
------------
Income
```

A higher ratio increases financial risk.

---

### 2. Credit Score

Applicants with lower credit scores receive a higher risk score.

---

### 3. Existing Loans

Applicants with multiple active loans are considered riskier borrowers.

---

### 4. Final Risk Score

The individual risk factors are combined into a normalized score.

```
0.0 ---------------------------> 1.0
Low Risk                    High Risk
```

---

### 5. Decision Logic

| Risk Score | Decision |
|------------|----------|
| < 0.30 | ✅ APPROVED |
| 0.30 – 0.70 | ⚠️ MANUAL_REVIEW |
| > 0.70 | ❌ REJECTED |

---

# 📡 API Reference

## POST `/predict`

### Request

```json
{
    "income": 1200000,
    "loanAmount": 500000,
    "creditScore": 780,
    "existingLoans": 1
}
```

---

### Response

```json
{
    "riskScore": 0.20,
    "approvalProbability": 0.80,
    "confidence": 0.90,
    "decision": "APPROVED",
    "reasons": [
        "Strong credit score",
        "Healthy debt-to-income ratio"
    ]
}
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/<username>/risk-engine.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Server

```bash
python app.py
```

The service will start on:

```
http://localhost:5000
```

---

# 🔄 Request Flow

```
Client
   │
   ▼
Spring Boot Backend
   │
   ▼
POST /predict
   │
   ▼
Flask Risk Engine
   │
   ▼
Risk Evaluation
   │
   ▼
Decision Generation
   │
   ▼
JSON Response
   │
   ▼
Spring Boot
   │
   ▼
Database
   │
   ▼
Frontend
```

---

# 🏗️ Design Decisions

### Modular Architecture

The project separates routing from business logic, making the codebase easier to maintain and extend.

### Explainable AI

Instead of returning only a decision, the engine also provides human-readable reasons to improve transparency.

### Independent Microservice

The Flask service operates independently from the Spring Boot backend, enabling separate deployment, scaling, and upgrades.

### API-First Design

The backend communicates exclusively through REST APIs, allowing the rule-based engine to be replaced with a machine learning model without changing the integration layer.

---

# 🔮 Future Enhancements

- Machine Learning Risk Model
- XGBoost / Random Forest Integration
- SHAP Explainability
- Fraud Detection Module
- Feature Engineering Pipeline
- Model Versioning
- Docker Containerization
- Kubernetes Deployment
- Prometheus & Grafana Monitoring

---

# 🛠️ Technology Stack

- Python
- Flask
- REST API
- JSON
- Modular Service Architecture

---

# 👨‍💻 Author

**Nishant**

Built as the AI underwriting component of the **FinSight AI** platform.
