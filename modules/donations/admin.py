from django.contrib import admin
from .models import Category, Donation, Payment, Cancellation, RelDonationCancellation

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


class DonationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Donation, DonationAdmin)


class PaymentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Payment, PaymentAdmin)


class CancellationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cancellation, CancellationAdmin)


class RelDonationCancellationAdmin(admin.ModelAdmin):
    pass


admin.site.register(RelDonationCancellation, RelDonationCancellationAdmin)
