from django.shortcuts import render, get_object_or_404
from .models import Category
from modules.organizations.models import Goal

# Create your views here.


def categories(request, id):
    categories = Category.objects.all()
    # organization = get_object_or_404(Organization, slug=slug, is_active=True)
    goal = get_object_or_404(Goal, id=id)
    return render(request, 'categories.html', {'categories': categories, 'goal': goal})


def amount_selection(request, id, slug):  # aquí debería crear una nueva Donation
    goal = get_object_or_404(Goal, id=id)
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'amount_selection.html', {'goal': goal, 'category': category})
