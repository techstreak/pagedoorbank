from django.urls import path
from . import views
from .views import AddBalanceView, send_money
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('account/', views.account_detail, name='account_detail'),
    path('send-money/', send_money, name='send_money'),
    path('users/', views.users, name='users'),
    
    path('add-balance/', AddBalanceView.as_view(), name='add_balance'),
    path('cash_out/', views.cash_out, name='cash_out'),
]
