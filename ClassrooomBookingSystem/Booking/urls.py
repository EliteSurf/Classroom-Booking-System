from django.urls import path
from . import views

urlpatterns = [
    path('Add/', views.add_booking, name='Add-Booking'),
    path('User/View/', views.user_view_booking, name='User-View-Booking'),
    path('Admin/View/', views.admin_view_booking, name='Admin-View-Booking'),
    path('Admin/View/<int:id>', views.admin_view_booking_detail, name='Admin-View-Booking-Detail'),
    path('Admin/Update/<int:id>', views.admin_update_booking_status, name='Admin-Update-Booking_Status')
]
