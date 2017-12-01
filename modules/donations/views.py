from django.shortcuts import render, get_object_or_404
from .models import Category, Donation
from modules.organizations.models import Goal
from modules.donations.forms import DonationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.core.context_processors import csrf

# Create your views here.


def categories(request, id):
    categories = Category.objects.all()
    # organization = get_object_or_404(Organization, slug=slug, is_active=True)
    goal = get_object_or_404(Goal, id=id)
    return render(request, 'categories.html', {'categories': categories, 'goal': goal})


# def amount_selection(request, id, slug):  # aquí debería crear una nueva Donation
#     goal = get_object_or_404(Goal, id=id)
#     category = get_object_or_404(Category, slug=slug)
#     return render(request, 'amount_selection.html', {'goal': goal, 'category': category})
#
#
# def donation(request):
#     if request.method == 'POST':
#         form = DonationForm(request.POST)
#         if form.is_valid():
#             amount = request.POST.get('amount', '')
#
#             donation_object = Donation(amount = amount)
#             donation_object.save()
#
#             return HttpResponseRedirect(reverse('donations:amount_selection'))  # nos debería mandar a paypal
#     else:
#         form = DonationForm()
#
#     return render(request, 'amount_selection.html', {'form': form})

# def thanks(request):
#     goal = get_object_or_404(Goal)
#
#     return render(request, 'thanks.html', {'goal': goal})


def donation(request, id, slug):
    goal = get_object_or_404(Goal, id=id)
    category = get_object_or_404(Category, slug=slug)

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            amount = request.POST.get('amount', '')
            organization = goal.organization
            donation_object = Donation(amount = amount, organization = organization, goal = goal, category = category)
            donation_object.save()

            # return HttpResponseRedirect(reverse('donations:thanks'))  # nos debería mandar a paypal, por ahora solo a página de agradecimiento
            return render(request, 'thanks.html', {'goal': goal,})
    else:
        form = DonationForm()

    return render(request, 'amount_selection.html', {'goal': goal, 'category': category, 'form': form})
