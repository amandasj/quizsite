from django.shortcuts import render

# Create your views here.

def startpage(request):
	return render(request, "quiz/index.html")

def quiz(request):
	return render(request, "quiz/startup.html")

def question(request):
	return render(request, "quiz/fragor.html")

def completed(request):
	return render(request, "quiz/resultat.html")



