from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_list, name='stock-list'),
    path('api/stocks/', views.stock_data_json, name='stock-json'),
    path('api/chart-data/<str:symbol>/', views.chart_data, name='chart_data'),

    path('api/price-history/<str:symbol>/', views.price_history_api, name='price_history_api'),
]
