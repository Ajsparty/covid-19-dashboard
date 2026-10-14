# COVID-19 Dashboard

Small dashboard I threw together to practice Plotly/Streamlit with the Johns Hopkins COVID data.

Currently just a demo with sample data. The full version I had in mind would pull live numbers and do choropleth + time series, but I only got the basic layout working before moving on.

## How to run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## What I actually finished
- Page config and title
- Button that loads a tiny sample dataframe
- Bar chart of confirmed cases

The data cleaning part was messier than I expected (lots of missing values and weird country names). Might come back to the map later.

MSU data science project, late 2024 / early 2025.