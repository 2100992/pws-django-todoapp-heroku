from django.contrib import admin

from tasks.models import TodoItem, Category


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_completed', 'created')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name','todos_count')
    list_display = ('slug', 'name')

