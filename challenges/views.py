from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges={
    "january":"Eat no meat for the entire mounth!",
    "february": "Walk for at leat 20 min a day!",
    "march":"Learn Django for at leat 20 min a day!",
    "april":"Eat no meat for the entire mounth!",
    "may": "Walk for at leat 20 min a day!",
    "june":"Learn Django for at leat 20 min a day!",
    "july":"Eat no meat for the entire mounth!",
    "august": "Walk for at leat 20 min a day!",
    "september":"Learn Django for at leat 20 min a day!",
    "october":"Eat no meat for the entire mounth!",
    "november": "Walk for at leat 20 min a day!",
    "december":"Learn Django for at leat 20 min a day!"
}
# Create your views here.

def index(request):
    list_items=""
    months=list(monthly_challenges.keys())
    for month in months:
        capitalized_month=month.capitalize()
        month_path=reverse("month-challenge", args=[month])
        list_items+=f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data=f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_number(request, month):
    months=list(monthly_challenges.keys())
    if month>len(month):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month=months[month-1]
    redirect_path=reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text=monthly_challenges[month]
        response_data=f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
