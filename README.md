# COVID-19 Analytics Dashboard

**Intermediate College-Level Data Visualization & Analytics Project**

## Project Description

An interactive, real-time dashboard built to explore and visualize the global COVID-19 pandemic. The application ingests Johns Hopkins University CSSE COVID-19 data and provides multiple analytical views including:

- Global choropleth map of confirmed cases and deaths
- Time-series trends with rolling averages
- Country comparison tool
- Statistical summary cards and growth rate calculations
- Simple forecasting using Prophet (optional extension)

This project highlights proficiency in data ingestion, transformation, interactive visualization, and dashboard deployment — core skills for any data scientist.

**Developed**: November 2024 – February 2025 as part of MSU Computational Data Science curriculum.

## Tech Stack
- Python (Pandas, NumPy)
- Plotly Dash (or Streamlit alternative)
- Plotly Express & Graph Objects for rich visualizations
- Pandas for ETL
- Optional: fbprophet for forecasting

## Key Features Implemented
- Responsive choropleth world map (daily updates simulated)
- Multi-line time series with date range selector
- Top 10 countries bar chart (cases/deaths)
- Growth rate calculator and 7-day moving average
- Downloadable filtered datasets (CSV)
- Dark/light theme toggle

## How to Run

```bash
git clone https://github.com/Ajsparty/covid-19-dashboard.git
cd covid-19-dashboard
pip install -r requirements.txt
python app.py   # or streamlit run app.py if using Streamlit version
```

Access the dashboard at `http://localhost:8050` (Dash) or the Streamlit port.

## Sample Insights Discovered
- Strong correlation between testing rates and reported cases in early 2021
- Several countries showed clear second and third waves in the time-series analysis
- European nations had significantly higher per-capita death rates during Delta variant period

## Learning Outcomes
- Mastering large-scale time-series data handling
- Creating publication-quality interactive visualizations
- Building maintainable dashboard architectures
- Understanding real-world data quality issues (missing values, reporting lags)

## Future Roadmap
- Integrate live API from disease.sh or WHO
- Add vaccination coverage overlays
- Machine learning component for case forecasting
- Deploy to Render or AWS Elastic Beanstalk

---

*By Aidan Swenson | Michigan State University | Computational Data Science*