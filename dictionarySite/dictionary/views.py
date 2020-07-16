from django.shortcuts import render, redirect
from django.http import HttpResponse
from PyDictionary import PyDictionary
from django.views.decorators.csrf import csrf_exempt
dictionary=PyDictionary()

@csrf_exempt
def index(request):
    print(dictionary.synonym('the'))
    if request.method == 'POST':
        print(request.POST['word'])
        return redirect('result/' + request.POST['word'])
    else:
        print('Error')
        return render(request, "home.html") 


@csrf_exempt
def result(request, word):
    context ={
        'word': word,
        'meaning' : dictionary.meaning(word),
        'synonym' : dictionary.synonym(word),
        'antonym' : dictionary.antonym(word),
        'wordType': list( dictionary.meaning(word).keys())
        # 'word': 'word',
        # 'meaning' : {'Noun': ['A', 'B', 'C'],
        #             'Adjective': ['A', 'B', 'C'],
        #             'Verb': ['A', 'B', 'C'],
        #             'Adverb': ['A', 'B', 'C']},
        # 'synonym' : ['SA', 'SB', 'SC'],
        # 'antonym' : ['AA', 'AB', 'AC'],
        # 'wordType': 'wordType'
        }
    
    return render(request, "result.html", context) 
