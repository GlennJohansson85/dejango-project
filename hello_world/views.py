from django.shortcuts import render

# Create your views here.
if request.method == "POST":
   return HttpResponse("You must have POSTed something")
else:
   Return HttpResponse(request.method)
