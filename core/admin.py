from django.contrib import admin
from .models import Page, PageVersion

class PageVersionInline(admin.TabularInline):
    model = PageVersion
    extra = 0
    readonly_fields = ('content', 'created_at')

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = [PageVersionInline] # Shows history inside the editor