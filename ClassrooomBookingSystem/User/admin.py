from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_identity', 'user', 'user_phone', 'user_role')

    def user_information(self, obj):
        return obj.user_name

    def get_user_data(self, request):
        query = super(UserProfileAdmin, self).get_queryset(request)
        query = query.order_by('user_name')
        return query

    user_information.short_description = 'user_name'


admin.site.register(UserProfile, UserProfileAdmin)