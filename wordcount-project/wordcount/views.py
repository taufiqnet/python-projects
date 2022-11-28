from django.http import HttpResponse
from django.shortcuts import render

# def homepage(request):
    # return HttpResponse('Hello')
def homepage(request):
    return render(request, 'home.html')

def wordcount(request):
    return render(request, 'wordcount.html')

def contact(request):
    return HttpResponse('<h1>This is Contact page</h1>')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    
    worddictionary = {}
    
    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #Add to dicionary
            worddictionary[word] = 1
    
    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'count_letter': len(fulltext), 'worddictionary':worddictionary.items()})