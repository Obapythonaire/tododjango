from django.contrib import admin
from .models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created')
    list_filter = ('title', 'creator', 'created')
    prepopulated_fields = {'body': ('title',)}

admin.site.register(Todo, TodoAdmin)
