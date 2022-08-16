
from django.contrib import admin

from app1.models import ApplicationSettings


# Register your models here.

# class ApplicationSettingsAdmin(admin.ModelAdmin):
#    fields = ('id','module','setting_name','setting_value','is_enabled')
#    list_display = ('id','module','setting_name','setting_value','is_enabled')


admin.site.register(ApplicationSettings)

