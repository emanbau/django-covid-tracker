from django.shortcuts import render

# Create your views here.
def helloworldview(request):
    return render(request, 'helloworld.html')
