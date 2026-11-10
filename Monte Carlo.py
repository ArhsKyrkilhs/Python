import numpy as np
import pandas as pd
import yfinance as yf

current_price = yf.Ticker("MSFT").fast_info['lastPrice'] #Feel free to change the stock (AAPL, NVDA, AMZN etc.)
money_invested = 10000
stocks_owned = money_invested / current_price

data = yf.download("MSFT", period="1y", interval="1d")   #Be sure to change it here too
prices = data['Close'] #Data of 1 year

simple_returns = prices.pct_change().dropna()

mu = simple_returns.mean()
sigma = simple_returns.std()
final_prices = []

mu_val = mu.iloc[0] if hasattr(mu, 'iloc') else mu              #Ensures μ is plain numbers
sigma_val = sigma.iloc[0] if hasattr(sigma, 'iloc') else sigma  #Ensures σ is plain numbers


S0 = current_price
num_simulations = 10000  # Number of future paths 
num_days = 10            # Time horizon (trading days)
dt = 1.0                 # Daily time step


for i in range(num_simulations):
    price = S0
    for day in range(num_days):
        Z = np.random.normal(0, 1)
        shock = (mu_val * dt) + (sigma_val * np.sqrt(dt) * Z)
        price = price * (1 + shock)
    final_prices.append(price)

# Calculate 95% Value at Risk (VaR)
pnl = np.array(final_prices) - S0
var_95 = np.percentile(pnl, 5) #You can also try changing the percentile here!

print(f"95% 10-day VaR: ${abs(var_95*stocks_owned):.2f}")
