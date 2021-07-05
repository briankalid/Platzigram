from django.contrib import admin

from .models import Profile
# Register your models here.
#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','username','phone_number','website','picture','is_active')

    list_display_links = ['pk','username','phone_number']
    list_editable = ['website','picture']
    
    search_fields = ['username','email','first_name','last_name','phone_number']
    
    list_filter=['is_staff','is_superuser','is_active','created','modified']

    #fieldsets=()

    #readonly_fields = ()
