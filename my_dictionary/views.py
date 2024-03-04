from django.shortcuts import render, redirect
from .models import Dictionary
from django.http import JsonResponse

# Create your views here.
def indexpage(request):
    return render(request, 'index.html', {'page': 'index'})

def addwordpage(request):
    if request.method == "GET":
        return render(request, 'add_word.html', {'page': 'add_word'})
    else:
        original = request.POST.get('original')
        translation = request.POST.get('translation')
        Dictionary.objects.create(original=original, translation=translation)
        return(redirect(addwordpage))

def wordslistpage(request):
    data = Dictionary.objects.all()
    if request.method == 'POST':
           entry_id = request.POST.get('id')
           try:
               entry = Dictionary.objects.get(id=entry_id)
               entry.delete()
               return JsonResponse({'success': True})
           except Dictionary.DoesNotExist:
               return JsonResponse({'success': False})       
    return render(request, 'words_list.html', {'page': 'words_list', 'data': data})
