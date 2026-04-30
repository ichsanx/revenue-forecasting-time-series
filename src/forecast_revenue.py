import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "monthly_revenue.csv"
MODEL_PATH = ROOT / "model" / "revenue_forecasting_model.joblib"
FORECAST_PATH = ROOT / "images" / "forecast_result.csv"

def build_features(df):
    df = df.copy()
    df["month"] = pd.to_datetime(df["month"])
    df["t"] = np.arange(len(df))
    df["month_num"] = df["month"].dt.month
    df["sin_12"] = np.sin(2 * np.pi * df["month_num"] / 12)
    df["cos_12"] = np.cos(2 * np.pi * df["month_num"] / 12)
    return df

def main():
    df = pd.read_csv(DATA_PATH)
    df = build_features(df)

    train = df.iloc[:-6]
    test = df.iloc[-6:]

    features = ["t", "sin_12", "cos_12"]
    model = LinearRegression()
    model.fit(train[features], train["revenue"])

    pred = model.predict(test[features])

    mae = mean_absolute_error(test["revenue"], pred)
    mape = mean_absolute_percentage_error(test["revenue"], pred)

    print("MAE :", round(mae, 2))
    print("MAPE:", round(mape, 4))

    future_dates = pd.date_range(
        df["month"].max() + pd.offsets.MonthBegin(1),
        periods=6,
        freq="MS"
    )

    future = pd.DataFrame({"month": future_dates})
    future["t"] = np.arange(len(df), len(df) + 6)
    future["month_num"] = future["month"].dt.month
    future["sin_12"] = np.sin(2 * np.pi * future["month_num"] / 12)
    future["cos_12"] = np.cos(2 * np.pi * future["month_num"] / 12)
    future["forecast_revenue"] = model.predict(future[features])

    print("\nForecast Result:")
    print(future[["month", "forecast_revenue"]])

    MODEL_PATH.parent.mkdir(exist_ok=True)
    FORECAST_PATH.parent.mkdir(exist_ok=True)

    joblib.dump(model, MODEL_PATH)
    future[["month", "forecast_revenue"]].to_csv(FORECAST_PATH, index=False)

    print(f"\nModel saved to: {MODEL_PATH}")
    print(f"Forecast saved to: {FORECAST_PATH}")

if __name__ == "__main__":
    main()
