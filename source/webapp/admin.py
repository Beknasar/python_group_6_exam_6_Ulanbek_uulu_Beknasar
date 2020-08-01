from django.contrib import admin
from .models import GuestBook


class GuestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'date_create')
    list_display_links = ('pk', 'name')
    list_filter = ('status',)
    search_fields = ('name',)


admin.site.register(GuestBook, GuestAdmin)
