from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']
    full_text2 = full_text.replace(",","").replace(".","")
    word_list = [x for x in full_text2.split(" ") if x != '']
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    return render(request, 'wordcount/count.html', \
                    {'fulltext': full_text, 'total': len(word_list), 'dict': word_dict.items()})