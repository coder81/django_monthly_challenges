from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
  "december": None
}

# Create your views here.
def index(request):
  months = list(monthly_challenges.keys())
  return render(request, "challenges/index.html", {
    "months": months
  })

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
    response_data = render(request, "challenges/challenge.html",{
      "text": challenge_text,
      "month_name": month
    })
    return HttpResponse(response_data)
  except:
    response_data = render_to_string("404.html")
    return HttpResponseNotFound(response_data)
  
  return HttpResponse(challenge_text)