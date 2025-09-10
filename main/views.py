from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_toko' : 'Fantasy Shop',
        'name': 'Muhammad Fattan Azzaka',
        'class': 'PBP B',
        'npm': '2406423276'
    }

    return render(request, "main.html", context)