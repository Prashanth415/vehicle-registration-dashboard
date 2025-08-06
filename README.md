# vehicle-registration-dashboard

1. ⚙️ Setup Instructions
🎯 To run the dashboard locally:

Clone the repo

Install dependencies using pip

Run the app with streamlit run main.py

2. Data Assumptions
This project uses synthetic data generated to simulate real-world vehicle registrations in India.

📊 Inspired by the Vahan Dashboard from the Ministry of Road Transport

🗓️ Covers data from 2020 to 2025

🚗 Includes 3 categories:

2W: Two-wheelers (Hero, Honda, TVS, Bajaj, Suzuki)

3W: Three-wheelers (Mahindra, Piaggio, Bajaj, Atul Auto)

4W: Four-wheelers (Maruti, Hyundai, Tata, Mahindra, Kia, Toyota)

📈 Each year assumes ~5% growth in vehicle registrations

🔄 Seasonal changes are simulated (e.g., Q1 has higher activity)

🎲 Random variation is added to make the data look realistic

📉 Calculated metrics:

YoY Growth = current quarter vs. same quarter last year

QoQ Growth = current quarter vs. previous quarter

3. Feature Roadmap
If this project is extended in the future, these features could be added:

🔌 Live API Integration: Connect directly to the Vahan Dashboard (if API access is possible)

🌍 State / District Filters: For region-specific analysis

📄 Export to Excel / PDF: Allow users to download graphs and reports

📈 Machine Learning Forecasting: Predict future registrations using models like ARIMA or Prophet

📱 Mobile-friendly UI: Improve layout for mobile and tablet users

🧾 Admin Data Upload: Let admins upload new data from CSV or Excel
