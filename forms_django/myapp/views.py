from django.shortcuts import render
from .forms import InputForm, MyForm
from .models import MyModel
from .serializer import MySerializer
from django.http import HttpResponse

def home_view(request):

    context = {}

    context["form"] = InputForm()

    return render(request, "index.html", context)

def myform(request):

    if request.method == "POST":
        form = MyForm(request.POST)

        if form.is_valid():
            form.save()
        
    else:
        form = MyForm()

    return render(request, "first.html", {"form": form})

        
def view_data(request):
    data = MyModel.objects.all()
    serialize = MySerializer(data, many = True)
    return HttpResponse(serialize.data)
