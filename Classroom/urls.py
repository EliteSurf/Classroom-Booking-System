from django.urls import path
from . import views


urlpatterns = [
    path('View/', views.view_classroom, name='View-Classroom'),
    path('Add/', views.add_classroom, name='Add-Classroom'),
    path('Edit/<int:id>', views.edit_classroom, name='Edit-Classroom'),
    path('Update/<int:id>', views.update_classroom, name='Update-Classroom'),
    path('Delete/<int:id>', views.delete_classroom, name='Delete-Classroom'),
    path('Booking_List/<int:id>', views.classroom_booking_list, name='Classroom-Booking-List'),
]