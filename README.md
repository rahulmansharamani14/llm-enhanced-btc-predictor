# LLM-Enhanced BTC Predictor

## Description
The **LLM-Enhanced BTC Predictor** is a machine learning project designed to predict Bitcoin prices using a combination of blockchain metrics, financial news sentiment analysis, and deep learning models. The project integrates data engineering, feature engineering, and advanced modeling techniques to provide accurate predictions and backtesting for investment strategies.

## Implementation Details

### Programming Languages
- **Python**: The primary language used for data processing, feature engineering, and model training.

### Key Components
1. **Data Collection**:
   - Fetches Bitcoin price data using `yfinance`.
   - Collects blockchain metrics such as hash rate, difficulty, and transaction volume.
   - Retrieves Bitcoin-related news headlines from the CryptoPanic API.

2. **Feature Engineering**:
   - Combines blockchain metrics and sentiment scores derived from financial news.
   - Generates lag features, moving averages, and volatility metrics.

3. **Sentiment Analysis**:
   - Utilizes the FinBERT model to classify news headlines into positive, neutral, or negative sentiments.
   - Maps sentiment labels to numerical scores for integration into the dataset.

4. **Modeling**:
   - Implements a baseline LSTM model for time-series forecasting.
   - Enhances predictions by incorporating sentiment features into the LSTM model.

5. **Backtesting**:
   - Simulates investment strategies using a custom backtesting engine.
   - Compares model performance against a buy-and-hold strategy.

### Dependencies
The project relies on the following Python libraries:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `tensorflow`
- `yfinance`
- `transformers`
- `requests`

For a complete list of dependencies, refer to the [requirements.txt](requirements.txt) file.

### Source Control
- **Version Control System**: Git
- **Repository**: The project is managed in a Git repository with `.gitignore` configured to exclude the virtual environment (`venv/`).

### Lines of Code
- **Total Lines of Code**: Approximately 2,500 (spread across notebooks, scripts, and utility files).

### Folder Structure
- **`notebooks/`**: Contains Jupyter notebooks for data exploration, feature engineering, and model training.
- **`src/`**: Includes Python scripts for reusable components like the backtesting engine.
- **`data/`**: Stores raw and processed datasets.
- **`.env`**: Contains API keys and sensitive configurations (excluded from version control).

## How to Run
1. Clone the repository:
```bash
   git clone <repository-url>
   cd llm-enhanced-btc-predictor
```

   
2. Start with Data Preprocessing
Open ```notebooks/01_data_preprocessing.ipynb``` to clean and merge the market, blockchain, and sentiment data.

3. Feature Engineering
Run ```feature_engineering.ipynb``` to create technical indicators, lags, and hybrid sentiment features.

4. Model Training
Use ```baseline_lstm.ipynb``` to train the LSTM model on your features dataset.

5. Sentiment Pipeline and Evaluate with Backtesting
If collecting new data, run ```sentiment_pipeline.ipynb``` to apply FinBERT and generate sentiment scores, simulating and analyzing model-driven trading strategies.




#### Key Results

- Best RMSE: ~2372
- Best Portfolio Return: $1398.47 vs $1241.70 (Buy & Hold)
- Win Rate: 51.38%



#### Highlights

- Combines blockchain activity with financial sentiment using LLMs
- Handles sparse sentiment data via synthetic augmentation
- Evaluated using both prediction accuracy and real-world financial simulation

#### Academic Use
This repository was created for academic learning only and does not constitute financial advice or production-ready trading code.