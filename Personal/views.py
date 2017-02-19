from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Personal/home.html')
def contact(request):
    return render(request, 'Personal/basic.html', {'content': ['If you want to cantact me, please email me','shanisean786@gmail.com']})
