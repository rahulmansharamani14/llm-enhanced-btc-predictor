import pandas as pd
import numpy as np

class BacktestEngine:
    def __init__(self, actual, predicted, initial_capital=1000):
        """
        actual: numpy array of true prices
        predicted: numpy array of predicted prices (same shape)
        """
        self.df = pd.DataFrame({
            "actual_today": actual[:-1],
            "actual_tomorrow": actual[1:],
            "predicted_tomorrow": predicted[1:]
        })
        self.initial_capital = initial_capital

    def run(self):
        # Decision: Buy if model says price will go up
        self.df["model_signal"] = self.df["predicted_tomorrow"] > self.df["actual_today"]

        # Daily return if bought
        self.df["price_change_pct"] = (
            self.df["actual_tomorrow"] - self.df["actual_today"]
        ) / self.df["actual_today"]

        self.df["model_daily_return"] = self.df["price_change_pct"] * self.df["model_signal"]

        # Portfolio growth
        self.df["model_cum_return"] = (1 + self.df["model_daily_return"]).cumprod() * self.initial_capital
        self.df["buyhold_cum_return"] = (1 + self.df["price_change_pct"]).cumprod() * self.initial_capital

        return self.df

    def summary(self):
        final_model = self.df["model_cum_return"].iloc[-1]
        final_bh = self.df["buyhold_cum_return"].iloc[-1]
        win_rate = self.df["model_signal"].mean() * 100

        print(f"📈 Model Final Portfolio: ${final_model:.2f}")
        print(f"📉 Buy & Hold Portfolio: ${final_bh:.2f}")
        print(f"Delta: ${final_model - final_bh:.2f}")
        print(f"Win Rate (buy signal days): {win_rate:.2f}%")
