# I have creted this file - Lakshay

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

    # return HttpResponse("""hello Lakshay <br> What do you want to do <a href="/charcount">charcount</a> <a href="/capfirst">capfirst</a>""")
def analyze(request):
        djtext = request.POST.get('text', 'default')
        removepunc = request.POST.get('removepunc', 'off')
        allincaps = request.POST.get('allcaps', 'off')
        newlineremove = request.POST.get('removeline', 'off')
        spaceremove = request.POST.get('removespace', 'off')
        charcounter = request.POST.get('charcounter', 'off')
        # print(djtext)
        # print(removepunc)   
        lst = [removepunc, allincaps, newlineremove, spaceremove, charcounter]
        if 'on' in lst:
                
                if removepunc == 'on':
                        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
                        djtext = "".join(i for i in djtext if i not in punc)
                        params = {'purpose': 'Remove Punctuation', "analyzed_text": djtext}
                        # return render(request, 'analyze.html', params)
                if allincaps == 'on':
                        djtext = djtext.upper()
                        params = {'purpose': 'UPPERCASE', "analyzed_text": djtext}
                        # return render(request, 'analyze.html', params)
                if newlineremove == 'on':
                        djtext = "".join(i for i in djtext if (i != "\n" and i != "\r"))
                        params = {'purpose': 'New line remove', "analyzed_text": djtext}
                        # return render(request, 'analyze.html', params)
                if spaceremove == 'on':
                        analyzed = ''
                        for index, i in enumerate(djtext):
                            if djtext[index] == " " and djtext[index+1] == " ":
                                pass
                            else:
                                analyzed += i
                        djtext = analyzed
                        params = {'purpose': 'Space Remover', "analyzed_text": djtext}
                        # return render(request, 'analyze.html', params)
                if charcounter == 'on':
                        n = len(djtext)
                        djtext += f"\nthe number of characters in the string is {n}" 
                params = {'purpose': 'Character Count', "analyzed_text": djtext}
                        # return render(request, 'analyze.html', params)
                return render(request, 'analyze.html', params)
                
        else:
                return HttpResponse("Error")

# d     f charcount(request):
#     return HttpResponse("about Lakshay")

# def capfirst(request):

#     return HttpResponse("about Lakshay")

# def spaceremover(request):

#     return HttpResponse("about Lakshay")

# def newlineremove(request):

#     return HttpResponse("about Lakshay")

