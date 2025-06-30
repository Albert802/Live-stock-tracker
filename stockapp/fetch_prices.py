import yfinance as yf
from django.utils.timezone import now
from .models import Stock, PriceHistory

def update_all_stocks():
    stocks = Stock.objects.all()
    symbols = [s.symbol for s in stocks if s.symbol]

    if not symbols:
        print("⚠️ No symbols to update.")
        return

    tickers = yf.Tickers(' '.join(symbols))

    for symbol, ticker in tickers.tickers.items():
        try:
            info = ticker.info
            price = info.get('regularMarketPrice')
            name = info.get('shortName')

            if price is not None:
                stock = Stock.objects.get(symbol=symbol)
                stock.last_price = price
                stock.updated_at = now()
                if name:
                    stock.name = name
                stock.save()

                # ✅ Log price in history after stock is updated
                PriceHistory.objects.create(stock=stock, price=price)

                print(f"✅ Updated {symbol}: {price}")
            else:
                print(f"⚠️ No price for {symbol}")
        except Exception as e:
            print(f"❌ Failed to update {symbol}: {e}")
