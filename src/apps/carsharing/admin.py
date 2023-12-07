from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'car_year', 'status')
    list_filter = ('status',)
    search_fields = ('car_brand', 'car_model', 'car_year')
    actions = ['make_busy', 'make_ready']

    def make_busy(self, request, queryset):
        queryset.update(status='BSY')

    def make_ready(self, request, queryset):
        queryset.update(status='RDY')

    make_busy.short_description = 'Mark selected cars as Busy'
    make_ready.short_description = 'Mark selected cars as Ready'

