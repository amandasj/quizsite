# coding: utf-8

from django.shortcuts import render

# Create your views here.

quizzes = {
	"klassiker": {
   		"name": u"Vad kan du om startups?",
	   	"description": u"Har du koll på dina startupkunskaper??"
	},
	"fotboll": {
	   	"name": u"Vilket företag byggde vilken produkt?",
	   	"description": u"Kan du para ihop rätt produkt med rätt företag?"
	},
	"kanda-hackare": {
	    	"name": u"Vad kan du om blablabla",
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





