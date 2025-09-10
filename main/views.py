from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title' : 'FeetBalls',
        'npm' : '2406398324',
        'name': 'Muhammad Nadhif Ibrahim',
        'class': 'PBP C',
        'shoes': 'Shoes',
        'ball': 'Balls',
        'jersey': 'Jersey'
    }

    return render(request, "main/main.html", context)