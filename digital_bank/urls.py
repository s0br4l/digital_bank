from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('newacc', views.newacc, name='newacc'),
    path('acclist', views.acclist, name='acclist'),
    path('acc/<acc_id>', views.accid, name='accid'),
    path('accbalance', views.accbalance, name='accbalance'),
    path('transactions', views.transactions, name='transactions'),
    path('acchistory', views.acchistory, name='acchistory'),
]
