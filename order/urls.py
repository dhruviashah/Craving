from django.urls import path, include
from order_delivery_integration.views import OrderDeliveryJoinView
from .views import (
	OrderView,
	order_display,
	customer_order_display,
	staff_order_display,
	staff_view_order,
	staff_display,
	delivery,
   deliver_order_display,
   deliver_order_detail,
   status_change,
   staff_order_history,
   staff_order_history_detail)

urlpatterns = [
   path('order',OrderView.as_view(),name='order_add'),
   path('order_display',order_display,name='order_display'),
   path('customer_order_display',customer_order_display,name='customer_order_display'),
   path('staff_order_display',staff_order_display,name='staff_order_display'),
   path('staff_view_order',staff_view_order,name='staff_view_order'),
   path('staff_display',staff_display,name='staff_display'),
   path('delivery',delivery,name='delivery'),
   path('delivery_entry',OrderDeliveryJoinView.as_view(),name='entry'),
   path('deliver_order_display',deliver_order_display,name='delivery'),  
   path('deliver_order_detail',deliver_order_detail,name='delivery'),
   path('status_change',status_change,name='status_change'),  

   path('staff_order_history',staff_order_history,name='staff_order_history'),
   path('staff_order_history_detail',staff_order_history_detail,name='staff_order_history_detail'),
]
