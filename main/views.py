from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("Helloworld!")

def test(request):
    return render(request, "test.html")
