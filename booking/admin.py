from django.contrib import admin
from .models import TravelOption, Booking

class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ('travel_id', 'type', 'source', 'destination', 'date_time')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'booking_date', 'status')

admin.site.register(TravelOption, TravelOptionAdmin)
admin.site.register(Booking, BookingAdmin)
