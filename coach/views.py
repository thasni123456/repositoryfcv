from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'coach/indexfans.html')
    
def indexcoach(request):
    return render(request,'coach/indexcoach.html')