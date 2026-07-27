# 🚚 FreightQuote AI – Intelligent Multi-Agent Logistics Platform

> An AI-powered logistics intelligence platform developed as part of the **Infosys Springboard Internship – Milestone 2**.

---

## 🌐 Live Demo

**Application URL**

https://hermelinda-intracardiac-alyse.ngrok-free.dev/

> **Note:** This application is hosted temporarily using **Google Colab + Streamlit + ngrok**. The public URL changes whenever the notebook is restarted.

---

# 📖 Project Overview

FreightQuote AI is a secure, AI-powered logistics platform that combines Machine Learning, Generative AI, and secure authentication into a single intelligent web application.

The platform helps logistics companies and supply chain managers:

- Predict freight transportation costs
- Estimate shipment delays
- Evaluate carrier compliance
- Securely manage users
- Interact with an AI Logistics Copilot
- Manage platform operations through an Admin Dashboard

The application is built using **Python**, **Streamlit**, **SQLite**, **Scikit-Learn**, **XGBoost**, **Hugging Face Transformers**, and **Google Colab**.

---

# 🎯 Project Objectives

The primary objectives of FreightQuote AI are:

- Build a secure AI-powered logistics platform.
- Integrate multiple Machine Learning models.
- Implement role-based authentication.
- Develop an interactive AI assistant.
- Provide intelligent logistics insights.
- Demonstrate practical use of Machine Learning in Supply Chain Management.

---

# 🚀 Key Features

## 🔐 Secure Authentication

- User Registration
- User Login
- Password Hashing
- Forgot Password
- Email OTP Verification
- JWT Authentication
- Session Management
- Account Locking
- Failed Login Tracking

---

## 👨‍💼 Admin Portal

The administrator has complete control over the platform.

### Features

- View Registered Users
- Delete User Accounts
- Unlock Locked Accounts
- Update User Roles
- Monitor Failed Login Attempts
- View Platform Statistics
- Monitor ML Model Status
- Manage System Health

---

## 👤 User Dashboard

Registered users can access:

- Dashboard
- AI Logistics Copilot
- Freight Prediction
- Delay Prediction
- Carrier Compliance Prediction
- Prediction History
- Secure Logout

---

# 🤖 AI Agents

FreightQuote AI consists of three intelligent AI agents.

---

## 🚛 Agent 1 – Freight Cost Prediction

### Purpose

Predicts the estimated freight transportation cost for a shipment.

### Input Features

- Shipment Mode
- Vendor
- Country
- Manufacturing Site
- Fulfillment Method
- Weight
- Line Item Quantity
- Unit Price
- Pack Price
- Line Item Value

### Output

Estimated Freight Cost

### Model

- XGBoost Regressor

---

## ⏱ Agent 2 – Route Delay Prediction

### Purpose

Predicts expected shipment delay based on logistics information.

### Input Features

- Shipping Mode
- Order Region
- Order State
- Market
- Customer Segment
- Product Price
- Scheduled Shipping Days
- Actual Shipping Days
- Order Quantity
- Benefit Per Order

### Output

Predicted Shipment Delay

### Model

- XGBoost Classifier

---

## 🛡 Agent 3 – Carrier Compliance Prediction

### Purpose

Predicts whether a carrier complies with logistics and operational standards.

### Input Features

- Product Type
- Availability
- Revenue
- Stock Levels
- Lead Time
- Shipping Time
- Route
- Transportation Mode
- Shipping Carrier
- Cost

### Output

Carrier Compliance Status

### Model

- Random Forest / XGBoost Classification Model

---

# 🤖 AI Logistics Copilot

The platform includes an AI-powered conversational assistant capable of answering logistics-related questions.

### Capabilities

- Freight Cost Guidance
- Route Suggestions
- Logistics Recommendations
- Shipment Planning
- Supply Chain Insights
- General Logistics Queries

Powered by:

- Hugging Face Transformers
- Qwen Language Model

---

# 🔐 Security Features

The application follows secure authentication practices.

## Authentication

- SHA-256 Password Hashing
- JWT Session Tokens
- Role-Based Access Control
- Admin Authorization
- Session Validation

---

## Account Protection

- Failed Login Counter
- Account Locking
- Password Recovery
- Email Verification

---

# 🗄 Database

SQLite Database

Stores:

- User Accounts
- Password Hashes
- User Roles
- Failed Login Attempts
- Account Status
- Prediction History

---

# 📊 Machine Learning Pipeline

```
Dataset
      │
      ▼
Preprocessing
      │
      ▼
Feature Encoding
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Model Serialization (.pkl)
      │
      ▼
Streamlit Prediction Interface
```

---

# 🏗 System Architecture

```
                    User

                      │

          Streamlit Web Interface

                      │

        Authentication & JWT Layer

                      │

         SQLite User Management

                      │

      -------------------------------

      │              │             │

Agent 1        Agent 2        Agent 3

      │              │             │

 Freight      Delay        Compliance

 Prediction  Prediction   Prediction

      │              │             │

      -------- AI Copilot ---------

                      │

              Hugging Face LLM
```

---

# 📁 Project Structure

```
FreightQuote_AI/

│

├── app.py

├── auth.py

├── database.py

├── config.py

├── predict.py

├── llm_engine.py

├── requirements.txt

├── freightquote.db

│

├── models/

│   ├── freight_price_model.pkl

│   ├── route_delay_model.pkl

│   ├── carrier_compliance_model.pkl

│   ├── agent1_label_encoders.pkl

│   ├── agent2_label_encoders.pkl

│   └── agent3_label_encoders.pkl

│

├── screenshots/

│

└── README.md
```

---

# ⚙ Technologies Used

## Programming

- Python 3.12

---

## Frontend

- Streamlit

---

## Backend

- SQLite
- JWT
- Hashlib

---

## Machine Learning

- Scikit-Learn
- XGBoost
- Joblib
- Pandas
- NumPy

---

## AI

- Hugging Face Transformers
- Qwen LLM

---

## Deployment

- Google Colab
- pyngrok
- Streamlit

---

# 🔑 Google Colab Secrets

The project securely stores sensitive information using Google Colab Secrets.

Required Secrets:

```
HF_TOKEN

JWT_SECRET

EMAIL_ADDRESS

EMAIL_PASSWORD

ADMIN_EMAIL_ID

ADMIN_PASSWORD

NGROK_AUTHTOKEN

KAGGLE_USERNAME

KAGGLE_KEY
```

---

# ▶ Running the Project

1. Open the notebook in Google Colab.
2. Add all required secrets in **Colab Secrets**.
3. Run all notebook cells from top to bottom.
4. Streamlit will start automatically.
5. An ngrok public URL will be generated.
6. Open the generated URL in your browser.
7. Register or log in to access the platform.

---

# 📈 Future Enhancements

- Real-Time Shipment Tracking
- Route Optimization using Reinforcement Learning
- Multi-language AI Assistant
- Cloud Deployment (AWS/Azure/GCP)
- Interactive Analytics Dashboard
- Voice-based Logistics Assistant
- Mobile Application
- API Integration with Logistics Providers
- Live Shipment Monitoring
- Predictive Inventory Management

---

# 👨‍💻 Developer

**Sai Laghuvar**

B.Tech – Computer Science & Engineering (IoT)

GITAM University, Bengaluru

Infosys Springboard Virtual Internship

---

# 📄 License

This project has been developed solely for educational and academic purposes as part of the Infosys Springboard Internship Program.

---

# 🙏 Acknowledgements

- Infosys Springboard
- GITAM University
- Google Colab
- Streamlit
- Hugging Face
- Scikit-Learn
- XGBoost
- Open Source Community

---

## ⭐ Thank You

Thank you for exploring **FreightQuote AI**.

If you found this project interesting, consider giving it a ⭐ on GitHub.
