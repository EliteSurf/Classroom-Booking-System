from django.contrib import admin
from .models import Classroom


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('classroom_identity', 'classroom_name', 'classroom_capacity', 'classroom_status')

    def classroom_information(self, obj):
        return obj.classroom_name

    def get_user_data(self, request):
        query = super(ClassroomAdmin, self).get_queryset(request)
        query = query.order_by('classroom_name')
        return query

    classroom_information.short_description = 'classroom_name'


admin.site.register(Classroom, ClassroomAdmin)
