from django.shortcuts import render, redirect
import random

def index(request):
    request.session['attempt'] = 0
    return render(request, "generator/index.html")

def generate(request):
    if "attempt" not in request.session:
        request.session['attempt'] = 1
    if request.method == "POST":
        random_word = ""
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
        for x in range(0, 14):
            random_word = random_word + str(random.choice(letters))
        words = {'random_word': random_word}
        print random_word
        request.session['attempt'] += 1
        return render(request, "generator/index.html", words)
    else:
        return redirect("/")

def reset(request):
    del request.session['attempt']
    return redirect('/')
# Create your views here.
