from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html', {'myhome': '这是我的博客'})
