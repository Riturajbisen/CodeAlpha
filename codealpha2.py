import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, quantity):
        self.portfolio[ticker] = {'quantity': quantity, 'purchase_price': yf.Ticker(ticker).history(period="1d")['Close'][0]}

    def remove_stock(self, ticker):
        if ticker in self.portfolio:
            del self.portfolio[ticker]

    def track_performance(self):
        for ticker, stock_data in self.portfolio.items():
            current_price = yf.Ticker(ticker).history(period="1d")['Close'][0]
            stock_data['current_price'] = current_price
            stock_data['profit_loss'] = (current_price - stock_data['purchase_price']) * stock_data['quantity']

    def display_portfolio(self):
        print("Your Stock Portfolio:")
        for ticker, stock_data in self.portfolio.items():
            print(f"Ticker: {ticker}")
            print(f"Quantity: {stock_data['quantity']}")
            print(f"Purchase Price: {stock_data['purchase_price']:.2f}")
            print(f"Current Price: {stock_data['current_price']:.2f}")
            print(f"Profit/Loss: {stock_data['profit_loss']:.2f}")
            print()

    def visualize_performance(self):
        data = []
        for ticker, stock_data in self.portfolio.items():
            data.append((ticker, stock_data['purchase_price'], stock_data['current_price']))

        df = pd.DataFrame(data, columns=['Ticker', 'Purchase Price', 'Current Price'])
        df.plot(kind='bar', x='Ticker', y=['Purchase Price', 'Current Price'], rot=45)
        plt.title('Stock Performance')
        plt.xlabel('Ticker')
        plt.ylabel('Price')
        plt.show()

# Example usage:
portfolio_tracker = StockPortfolioTracker()
portfolio_tracker.add_stock("AAPL", 100)
portfolio_tracker.add_stock("GOOGL", 50)
portfolio_tracker.track_performance()
portfolio_tracker.display_portfolio()
portfolio_tracker.visualize_performance()
