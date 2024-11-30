from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',) 
    list_editable = ('description')
    list_display_links = ('name')
    list_per_page = 20
    ordering = ('-created_at')
    actions = ['delete_selected_tasks']

    def delete_selected_tasks(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f'{count} задача(-и) успешно удалены')

    delete_selected_tasks.short_description = 'Удалить выбранные задачи'

    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Дополнительная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ('created_at',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'category')
    
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Дополнительная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ('created_at',)
