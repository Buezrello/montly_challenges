from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    'january': 'Eat no meat all month',
    'february': 'Walk at least 20 minutes every day',
    'march': 'Learn Django every day'
}


def monthly_challenge_by_number(request, month):

    if month < 1 or month > len(monthly_challenges):
        return HttpResponseNotFound('Invalid month number')

    months = list(monthly_challenges.keys())

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenge/januare

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound('This month is not supported')

    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    
    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)
