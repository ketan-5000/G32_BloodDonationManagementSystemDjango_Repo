from django.contrib import admin
from .models import BloodDonation, BloodRequest

class BloodDonationAdmin(admin.ModelAdmin):
    list_display = ('get_donor_name', 'blood_group', 'amount', 'donation_date', 'city')
    search_fields = ('donor__name', 'blood_group', 'city')
    list_filter = ('blood_group', 'city', 'donation_date')
    date_hierarchy = 'donation_date'

    def get_donor_name(self, obj):
        return obj.donor.name
    get_donor_name.short_description = 'Donor Name'

class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('blood_group',)
    search_fields = ('blood_group',)
    list_filter = ('blood_group',)

admin.site.register(BloodDonation, BloodDonationAdmin)
admin.site.register(BloodRequest, BloodRequestAdmin)
