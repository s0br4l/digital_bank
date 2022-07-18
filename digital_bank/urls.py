from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('newacc', views.newacc, name='newacc'),
    path('acclist', views.acclist, name='acclist'),
    path('acc/<acc_id>', views.accid, name='accid'),
    path('accbalance', views.accbalance, name='accbalance'),
    path('accbalance_results', views.accbalance_results, name='accbalance_results'),
    path('transactions', views.transactions, name='transactions'),
    path('transactions_results', views.transactions_results, name='transactions_results'),
    path('acchistory', views.acchistory, name='acchistory'),
]
