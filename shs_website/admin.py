from django.contrib import admin
from .models import Post, AddFacultyModel, EventDetail, NotificationsModel

# Register your models here.
admin.site.register(AddFacultyModel)
admin.site.register(EventDetail)
admin.site.register(Post)
admin.site.register(NotificationsModel)