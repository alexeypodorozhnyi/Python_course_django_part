from django.urls import path

from .views import ItemList, ShoppingEventCreate, ReversalList, BoughtItemList, ItemUpdate, ItemCreate, ReversalCreate, ReversalConfirm, ReversalDecline

urlpatterns = [
    path('', ItemList.as_view(), name='item_list_url'),
    path('shopping/', ShoppingEventCreate.as_view(), name='shopping_url'),
    path('reversal_list/', ReversalList.as_view(), name='reversal_list_url'),
    path('bought_list/', BoughtItemList.as_view(), name='bought_list_url'),
    path('item_create/', ItemCreate.as_view(), name='item_create_url'),
    path('item_update/<int:pk>/', ItemUpdate.as_view(), name='item_update_url'),
    path('reversal_create/', ReversalCreate.as_view(), name='reversal_create_url'),
    path('reversal_update/<int:pk>/', ReversalConfirm.as_view(), name='reversal_update_url'),
    path('reversal_decline/<int:pk>/', ReversalDecline.as_view(), name='reversal_decline_url'),
]
