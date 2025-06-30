from django.shortcuts import render
from .models import Stock, PriceHistory
from django.http import JsonResponse

def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stockapp/stock_list.html', {'stocks': stocks})

def stock_data_json(request):
    data = list(Stock.objects.values('symbol', 'name', 'last_price', 'updated_at'))
    return JsonResponse({'stocks': data})

def chart_data(request, symbol):
    stock = Stock.objects.get(symbol=symbol.upper())
    history = PriceHistory.objects.filter(stock=stock).order_by('-timestamp')[:20]
    history = reversed(history)  # so it's in chronological order

    labels = [p.timestamp.strftime("%H:%M:%S") for p in history]
    prices = [p.price for p in history]

    return JsonResponse({
        'labels': labels,
        'prices': prices,
        'symbol': stock.symbol
    })

def price_history_api(request, symbol):
    try:
        stock = Stock.objects.get(symbol=symbol)
        history = PriceHistory.objects.filter(stock=stock).order_by('-timestamp')[:20][::-1]  # latest 20, in chronological order
        data = {
            "timestamps": [entry.timestamp.strftime('%H:%M:%S') for entry in history],
            "prices": [entry.price for entry in history],
        }
        return JsonResponse(data)
    except Stock.DoesNotExist:
        return JsonResponse({"error": "Stock not found"}, status=404)


