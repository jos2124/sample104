from django.shortcuts import render

# Create your views here.
def sample_view(request):
    return render(request,'testapp/results.html')


def sample_sports(request):
    return render(request,'testapp/sports.html')
