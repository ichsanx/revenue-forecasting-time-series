# Revenue Forecasting Using Time Series Analysis

Project ini bertujuan untuk memprediksi revenue periode berikutnya menggunakan pendekatan **time series forecasting**. Project ini relevan untuk posisi Data Scientist, Business Intelligence Analyst, Revenue Analyst, dan Data Analyst.

## Business Problem

Perusahaan membutuhkan proyeksi revenue untuk membantu penyusunan target penjualan, perencanaan kapasitas, evaluasi pertumbuhan bisnis, dan pengambilan keputusan strategis.

## Dataset

Dataset pada folder `data/` adalah **synthetic monthly revenue data** untuk kebutuhan portofolio. Dataset dapat diganti dengan data revenue real perusahaan.

Kolom utama:
- `month`
- `revenue`

## Methodology

1. Data understanding
2. Time series visualization
3. Trend analysis
4. Seasonality feature engineering
5. Train-test split berbasis waktu
6. Forecasting model
7. Model evaluation
8. Business recommendation

## Model

Model utama:
- Linear Regression with trend and seasonality features

Model alternatif yang bisa dikembangkan:
- Moving Average
- ARIMA
- SARIMA
- Prophet
- XGBoost Regressor

## Evaluation Result

Baseline result pada synthetic data:

| Metric | Score |
|---|---:|
| MAE | 5,643,424 |
| MAPE | 2.35% |

## Business Insight

Forecasting revenue membantu perusahaan melihat estimasi pendapatan beberapa bulan ke depan. Hasil ini dapat digunakan untuk menentukan target revenue, menyesuaikan strategi penjualan, dan mengantisipasi periode dengan potensi penurunan pendapatan.

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

```bash
pip install -r requirements.txt
python src/forecast_revenue.py
```

Atau buka notebook:

```bash
jupyter notebook notebook/revenue_forecasting.ipynb
```

## Portfolio Summary for CV

Created a revenue forecasting model using historical monthly revenue data to identify trends, seasonality, and future revenue projection. The analysis supports business planning, sales target setting, and revenue growth strategy.
