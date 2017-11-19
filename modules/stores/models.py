from django.db import models
import uuid
# from modules.locations.models import Location
from modules.users.models import User
from modules.donations.models import Donation, Category
from modules.organizations.models import Organization

# Create your models here.


class StoreType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return


class Store(models.Model):
    storetype = models.ForeignKey(StoreType)
    # location = models.OneToOneField(Location)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return


class Coupon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category)
    store = models.ForeignKey(Store)
    organization = models.ManyToManyField(Organization)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField()
    valid_from = models.DateField()
    valid_until = models.DateField()
    image = models.URLField()
    is_active = models.BooleanField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return


class RelUserCouponDonation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey(Store)
    user = models.ForeignKey(User)
    donation = models.OneToOneField(Donation)
    coupon = models.ForeignKey(Coupon)

    def __str__(self):
        return self.id

    def __unicode__(self):
        return
