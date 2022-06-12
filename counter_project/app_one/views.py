from django.shortcuts import render, HttpResponse,redirect
def index(request):
    if "counter" in request.session:
        counter = request.session["counter"]
    else:
        counter = 0
        request.session["counter"] = 0
    request.session["counter"] = counter +1 
    context = {
        "counter": counter
    }
    return render(request, 'index.html', context=context)

def clear(request):
    request.session["counter"] = 0
    return redirect("/")
