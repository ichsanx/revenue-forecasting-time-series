# Revenue Forecasting Using Time Series Analysis

This project aims to forecast future revenue using a **time series forecasting** approach. It is relevant for Data Scientist, Business Intelligence Analyst, Revenue Analyst, and Data Analyst roles.

## Business Problem

Companies need revenue projections to support sales target planning, capacity planning, business growth evaluation, and strategic decision-making.

## Dataset

The dataset in the `data/` folder contains **synthetic monthly revenue data** for portfolio purposes. It can be replaced with real company revenue data when available.

Main columns:

- `month`
- `revenue`

## Methodology

1. Data understanding
2. Time series visualization
3. Trend analysis
4. Seasonality feature engineering
5. Time-based train-test split
6. Forecasting model development
7. Model evaluation
8. Business recommendation

## Model

Main model:

- Linear Regression with trend and seasonality features

Alternative models for future development:

- Moving Average
- ARIMA
- SARIMA
- Prophet
- XGBoost Regressor

## Evaluation Result

Baseline result on synthetic data:

| Metric | Score |
|---|---:|
| MAE | 5,643,424 |
| MAPE | 2.35% |

## Business Insight

Revenue forecasting helps companies estimate revenue for the upcoming months. The results can be used to set revenue targets, adjust sales strategies, and anticipate periods with potential revenue decline.

## Project Structure

```text
revenue-forecasting-time-series/
├── data/
│   └── monthly_revenue.csv
├── notebook/
│   └── revenue_forecasting.ipynb
├── src/
│   └── forecast_revenue.py
├── model/
│   └── revenue_forecasting_model.joblib
├── images/
│   ├── revenue_trend.png
│   ├── forecast_result.png
│   └── forecast_result.csv
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the forecasting script:

```bash
python src/forecast_revenue.py
```

Or open the notebook:

```bash
jupyter notebook notebook/revenue_forecasting.ipynb
```

## Portfolio Summary for CV

Created a revenue forecasting model using historical monthly revenue data to identify trends, seasonality, and future revenue projections. The analysis supports business planning, sales target setting, and revenue growth strategy.
