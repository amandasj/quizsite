# coding: utf-8

from django.shortcuts import render

# Create your views here.

quizzes = {
	"klassiker": {
   		"name": u"Klassiska böcker",
	   	"description": u"Hur bra kan du dina klassiker?"
	},
	"fotboll": {
	   	"name": u"Största fotbollslagen",
	   	"description": u"Kan du dina lag?"
	},
	"kanda-hackare": {
	    	"name": u"Världens mest kända hackare",
	    	"description": u"Hackerhistoria är viktigt, kan du den?"	},
}

def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/index.html", context)

def quiz(request, slug):
	context = {
		"quiz": quizzes[slug],
		“quiz_slug”: slug,
	}
	return render(request, "quiz/startup.html", context)

def question(request):
	return render(request, "quiz/fragor.html")

def completed(request):
	return render(request, "quiz/resultat.html")





