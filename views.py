from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render,redirect


def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text from input
    dj_text = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    analyzed = ""
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    
    if removepunc == 'on':
        
        for i in dj_text:
            if i not in punctuations:
                analyzed += i

        params = {'purpose':'Remove Punctuations','analyzed_text': analyzed}
        return render(request,'analyze.html', params)
    elif fullcaps == 'on':
        analyzed=""
        for i in dj_text:
            if i not in punctuations:
                analyzed += i
        params = {'purpose':'Captalize Text','analyzed_text': analyzed.upper()}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")

def capitalize(request):
    return HttpResponse("Capitalize")

def lineremove(request):
    return HttpResponse("Line Remove")

def spaceremove(request):
    return HttpResponse("Space Remover <a href='/'>back</a>")

def char_count(request):
    return HttpResponse("Character Counter")