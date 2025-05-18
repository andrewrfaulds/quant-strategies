
📈 Bollinger Band Strategy – Backtrader + yFinance

This repository contains a basic Bollinger Band mean-reversion trading strategy implemented using Backtrader and yFinance.

It demonstrates how to:

    Download historical stock data using yfinance

    Feed that data into Backtrader using PandasData

    Implement a simple Bollinger Band strategy

    Visualize trades and portfolio performance

📜 Strategy Logic

The strategy uses a 20-period Bollinger Band with a standard deviation factor of 2.0.

    Buy Signal: When the current price closes below the lower Bollinger Band → a long trade is opened.

    Sell Signal: When the price closes above the upper Bollinger Band → the trade is closed.

There are no stop-losses or trailing exits, so this is a raw demonstration of mean-reversion behavior.
📊 What the Chart Shows

After running the script, a matplotlib window will display the backtest results.

You’ll see:

    🟢 Green triangles: Buy entries

    🔴 Red triangles: Sell exits

    ⚫ Black line: AAPL price

    🔺 Red bands: The upper and lower Bollinger Bands

    💰 Blue/red markers: Profit/loss per trade

    🪙 Cash & portfolio value lines at the top

This helps visualize the performance and behavior of the strategy over time.
⚙️ Requirements

Install dependencies:

pip install backtrader yfinance pandas matplotlib

🚀 Usage

Run:

python bollinger_band_strategy.py

A chart will appear after the backtest completes.
📁 File List

    bollinger_band_strategy.py: The full working strategy

    requirements.txt: Dependencies list
