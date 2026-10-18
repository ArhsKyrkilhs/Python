import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf


returns = yf.download('AAPL', start='2020-01-01', progress=False)[
    'Close'
].pct_change().dropna()
returns_array = returns.values.flatten()


fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.canvas.manager.set_window_title('Central Limit Theorem with stocks')
sample_sizes = [1, 5, 20, 50]

for ax, n in zip(axes.flatten(), sample_sizes):

  means = [
      np.mean(np.random.choice(returns_array, size=n)) for _ in range(5000)
  ]

  ax.hist(means, bins=30, density=True, color='skyblue', edgecolor='black')
  ax.set_title(f'N = {n} days')

plt.tight_layout()
plt.show()