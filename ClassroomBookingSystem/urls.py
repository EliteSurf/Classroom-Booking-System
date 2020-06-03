from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Admin/', admin.site.urls),
    path('', include('Index.urls')),
    path('User/', include('User.urls')),
    path('Classroom/', include('Classroom.urls')),
    path('Booking/', include('Booking.urls')),
]
