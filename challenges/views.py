from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
  "january": "Eat no meat for entire month!",
  "february": "Walk for af least 20 minutes every day!",
  "march": "Eat no meat for entire month!",
  "april": "Eat no meat for entire month!",
  "may": "Eat no meat for entire month!",
  "june": "Eat no meat for entire month!",
  "july": "Eat no meat for entire month!",
  "august": "Eat no meat for entire month!",
  "september": "Eat no meat for entire month!",
  "october": "Eat no meat for entire month!",
  "november": "Eat no meat for entire month!",
  "december": "Eat no meat for entire month!"
}

# Create your views here.
def index(request):
  list_items = ""
  months = list(monthly_challenges.keys())
  for month in months:
    capitalized_month = month.capitalize()
    month_path = reverse("month-challenge", args=[month])
    list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
  response_data = f"<ul>{list_items}</ul>"
  return HttpResponse(response_data)

def monthly_challenge_by_number(request,month):
  months = list(monthly_challenges.keys())
  if month > len(months):
    return HttpResponseNotFound("This month is not supported!")

    return HttpResponseNotFound("This month is not supported!")
  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenge", args=[redirect_month])
  return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    response_data = f"<h2>{challenge_text}</h2>"
  except:
    return HttpResponseNotFound("This month is not supported!")
  return HttpResponse(challenge_text)