from django.contrib import admin
from .models import Catagory, Book
# Register your models here.
admin.site.register(Book)
class catagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'slug']

admin.site.register(Catagory, catagoryAdmin)
