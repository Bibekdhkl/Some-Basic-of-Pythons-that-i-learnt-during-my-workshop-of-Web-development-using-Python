from django.shortcuts import render
from news.models import NewCategory,News
from news.forms import NewsForm
def home(request):

    x=NewCategory.objects.all()
    form = NewsForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()#only in server side then if client side then it needs to use javascript code
    context = {
        'a':x,
        'form':form
    }
    return render(request,'index.html',context)
def list(request):
    return render(request,'news.html')