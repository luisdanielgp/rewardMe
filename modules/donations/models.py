from django.db import models
import uuid
from modules.organizations.models import Organization, Goal
from modules.users.models import User
from django.core.urlresolvers import reverse


# Create your models here.

STATUSES = (
    ('CPT', 'Completed'),
    ('PND', 'Pending'),
    ('CNCL', 'Cancelled')
)


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, db_index=True)
    start = models.DecimalField(decimal_places=2, max_digits=6)
    end = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return

    # def get_absolute_url(self):
    #     return reverse('donations:amount_selection', args=[self.id])


class Donation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization)
    goal = models.ForeignKey(Goal)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=50, choices=STATUSES)

    def __str__(self):
        return self.amount

    def __unicode__(self):
        return


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User)
    donation = models.OneToOneField(Donation)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=80)  # checar de paypal

    def __str__(self):
        return self.amount

    def __unicode__(self):
        return


class Cancellation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()

    def __str__(self):
        return self.description

    def __unicode__(self):
        return


class RelDonationCancellation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cancellation = models.OneToOneField(Cancellation)
    donation = models.OneToOneField(Donation)

    def __str__(self):
        return self.id

    def __unicode__(self):
        return
