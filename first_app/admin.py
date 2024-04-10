from django.contrib import admin
from .models import First_app

class First_AppAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'joined_date',)

admin.site.register(First_app, First_AppAdmin)