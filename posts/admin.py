from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class post(admin.ModelAdmin):
    pass

