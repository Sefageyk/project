from django.shortcuts import render
from .models import Category, Movie
from django.shortcuts import render, get_object_or_404

kategori_liste = ["macera","korku","dram","bilim kurgu", "komedi"]
film_liste = [
    {
        "id": 1,
        "film_adi": "film 1",
        "aciklama": "film 1 açıklama",
        "resim": "1.jpeg",
        "kategori": "macera",
        "anasayfa": True
    },
     {
        "id": 2,
        "film_adi": "film 2",
        "aciklama": "film 2 açıklama",
        "resim": "2.jpeg",
        "kategori": "dram",
        "anasayfa": False
    },
    {
        "id": 3,
        "film_adi": "film 3",
        "aciklama": "film 3 açıklama",
        "resim": "3.jpeg",
        "kategori": "korku",
        "anasayfa": False
    },
    {
        "id": 4,
        "film_adi": "film 4",
        "aciklama": "film 4 açıklama",
        "resim": "4.jpeg",
        "kategori": "komedi",
        "anasayfa": False
    }  
]

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.filter(anasayfa=True)
    }
    return render(request, "index.html", data)

def movies(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all()
    }
    return render(request, "movies.html", data)

def moviedetails(request, id):
    data = {
        "movie": Movie.objects.get(id=id)
    }
    return render(request, "details.html", data)

def kategori_detay(request, kategori_id):
    kategori = get_object_or_404(kategori_liste, pk=kategori_id)
    filmler = film_liste(kategori=kategori)
    return render(request, 'filmler/kategori_detay.html', {'kategori': kategori, 'filmler': filmler})