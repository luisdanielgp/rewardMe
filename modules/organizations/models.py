from django.db import models
import uuid

# Create your models here.


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField()
    # goal = models.TextField()
    logo = models.URLField()
    video = models.URLField(blank=True)
    donations_number = models.IntegerField(blank=True)
    is_active = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=("Date Created"))
    date_modified = models.DateTimeField(auto_now=True, verbose_name=("Date Modified"))

    def __str__(self):
        return self.name

    def __unicode__(self):
        return


class Period(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return


class Goal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE)
    period = models.ForeignKey(Period)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    def __unicode__(self):
        return
