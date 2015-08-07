# coding: utf-8

from django.shortcuts import render

# Create your views here.

from quiz.models import Quiz

def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/index.html", context)

def quiz(request, slug):
	context = {
		"quiz": quizzes[slug],
		"quiz_slug": slug,
	}
	return render(request, "quiz/startup.html", context)

def question(request, slug, number):
	context = {
		"question_number": number,
	    	"question": u"Hur många användare har Spotify?",
		"answer1": u"10 miljoner",
	   	"answer2": u"40 miljoner",
	    	"answer3": u"70 miljoner",
	    	"quiz_slug": slug,
	}
	return render(request, "quiz/fragor.html", context)


def completed(request, slug):
	context = {
	    	"correct": 12,
	    	"total": 20,
		"quiz_slug": slug,
	}
	return render(request, "quiz/resultat.html", context)





