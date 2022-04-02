from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('top_seller', 'name', 'email', 'date_hired')
    list_display_links = ('name',)
    search_fields = ('name', )
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
