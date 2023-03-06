from django.contrib import admin

# Register your models here.
from firstapp.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    # model=Profile
    list_display=['user','first_name','last_name']


admin.site.register(Profile, ProfileAdmin)