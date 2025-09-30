from django.urls import path
from . import views

urlpatterns = [
    path('quote/<str:symbol>/', views.get_symbol_quote, name='get_symbol_quote'),
    path('nifty50/', views.get_nifty_50_ltp, name='get_nifty_50_ltp'),
    path('health/', views.health_check, name='health_check'),
]
