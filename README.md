# Reddit QA & Automation Testing Suite

This repository demonstrates a comprehensive Quality Assurance approach applied to the Reddit platform. It covers UI Automation, Performance/Stress Testing, and Backend Data Validation.

## 🚀 Key Features
- **UI Automation:** Built with **Python** & **Selenium** using **Page Object Model (POM)** for high maintainability.
- **Performance Testing:** Load and Stress testing scripts using **Locust** and **JMeter** to analyze system bottlenecks.
- **Backend Testing:** Complex **SQL** queries for verifying data integrity and consistency.
- **API Validation:** Functional testing of Reddit's JSON endpoints.

## 🛠 Tech Stack
- **Language:** Python 3.x
- **Frameworks:** PyTest, Selenium WebDriver
- **Performance Tools:** Locust, JMeter
- **Database:** SQL (PostgreSQL/MySQL)
- **CI/CD & Tools:** Git, GitHub, Jira, Postman

## 📁 Project Structure
- `pages/`: Page Object classes defining UI elements and actions.
- `tests/`: Automated test cases for functional UI testing.
- `performance/`: Locust scripts for simulating concurrent user loads.
- `sql/`: SQL scripts for backend data verification.

## ⚙️ How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run UI tests: `pytest tests/`
3. Run Performance tests: `locust -f performance/locust_test.py`

---
**Author:** [Adın Soyadın]
**LinkedIn:** [LinkedIn Linkin]
