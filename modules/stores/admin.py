from django.contrib import admin
from .models import StoreType, Store, Coupon, RelUserCouponDonation

# Register your models here.


class StoreTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(StoreType, StoreTypeAdmin)


class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Store, StoreAdmin)


class CouponAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Coupon, CouponAdmin)


class RelUserCouponDonationAdmin(admin.ModelAdmin):
    pass


admin.site.register(RelUserCouponDonation, RelUserCouponDonationAdmin)
