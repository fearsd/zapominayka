from django.contrib import admin

from app.admin import ModelAdmin
from .models import Author

# Register your models here.
admin.site.register(Author)
