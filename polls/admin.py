from django.contrib import admin

# Register your models here.
from .models import inviteMarried_request
admin.site.site_header='WELCOME'

class inviteMarried_request_Admin(admin.ModelAdmin):
    search_fields=['maleName']    



admin.site.register(inviteMarried_request,inviteMarried_request_Admin)
