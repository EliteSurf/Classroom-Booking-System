from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_identity', 'get_user_name', 'get_classroom_name', 'booking_date', 'booking_time',
                    'booking_category', 'booking_reason', 'booking_status')

    def get_booking_data(self, request):
        query = super(BookingAdmin, self).get_queryset(request)
        query = query.order_by('booking_identity')
        return query

    def get_user_name(self, obj):
        return obj.booking_user_identity.userprofile.user_name

    get_user_name.short_description = 'User'

    def get_classroom_name(self, obj):
        return obj.booking_classroom_identity.classroom_name

    get_classroom_name.short_description = 'Classroom'


admin.site.register(Booking, BookingAdmin)
