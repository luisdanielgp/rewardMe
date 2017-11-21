from django.shortcuts import render, get_object_or_404
from .models import Organization
from modules.donations.views import categories
from modules.donations.models import Category

# Create your views here.


def organizations(request):
    organizations = Organization.objects.filter(is_active=True)
    return render(request, 'organizations.html', {"organizations": organizations})


def organization_details(request, slug):
    organization = get_object_or_404(Organization, slug=slug, is_active=True)
    goals = organization.goal_set.all()
    return render(request, 'organization_details.html', {'organization': organization, 'goals': goals})
