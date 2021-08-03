from django.http.response import HttpResponseNotModified
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    'january': 'Eat no meat all month',
    'february': 'Walk at least 20 minutes every day',
    'march': 'Learn Django every day',
    'april': None
}


def monthly_challenge_by_number(request, month):

    if month < 1 or month > len(monthly_challenges):
        return HttpResponseNotFound('Invalid month number')

    months = list(monthly_challenges.keys())

    redirect_month = months[month-1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/januare

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        raise Http404()

    return render(request, "challenges/challenge.html", {
        "month": month,
        "challenge_text": challenge_text
    })


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
