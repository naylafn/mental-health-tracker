from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306213426',
        'name': 'Nayla Farah Nida',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)