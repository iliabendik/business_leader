from django.shortcuts import render
from .models import Company
from .models import City
from .models import Uslugi_dla_biznesa
from .models import Tovari_dla_biznesa
from .models import Investicii
#from .models import Kommercheskie_tenderi
from .models import Meri_podderjki
from .models import Pervaya_socialnaya_birja
#from .models import Socialnie_projekti
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.db.models import Q

class CompaniesView(ListView):
    def get(self, request):
        def dic_creation(Class):
            x = {str(el.id): el.name for el in Class.objects.all()}
            return x

        companies = Company.objects.all()
        city = City.objects.all()
        city_dic=dic_creation(City)
        uslugi_dla_biznesa = Uslugi_dla_biznesa.objects.all()
        uslugi_dla_biznesa_dic=dic_creation(Uslugi_dla_biznesa)
        tovari_dla_biznesa = Tovari_dla_biznesa.objects.all()
        tovari_dla_biznesa_dic = dic_creation(Tovari_dla_biznesa)



        city_out = 'Город'
        uslugi_dla_biznesa_out = 'Услуги для бизнеса'
        tovari_dla_biznesa_out = 'Товары для бизнеса'
        if request.method == 'GET':
            city_get = request.GET.getlist('city')
            uslugi_dla_biznesa_get = request.GET.getlist('uslugi_dla_biznesa')
            tovari_dla_biznesa_get = request.GET.getlist('tovari_dla_biznesa')


            try:
                city_out=city_dic[city_get[0]]
            except:
                pass

            try:
                uslugi_dla_biznesa_out = uslugi_dla_biznesa_dic[uslugi_dla_biznesa_get[0]]
            except:
                pass

            try:
                tovari_dla_biznesa_out = tovari_dla_biznesa_dic[tovari_dla_biznesa_get[0]]
            except:
                pass

            companies = Company.objects.filter(place__in=city_get) \
                .filter(Q(category_uslugi_dla_biznesa__in=uslugi_dla_biznesa_get) | Q(
                category_tovari_dla_biznesa__in=tovari_dla_biznesa_get))

        return render(request, 'main/supreme.html', {'city_out':city_out,
                                                     'uslugi_dla_biznesa_out': uslugi_dla_biznesa_out,
                                                     'tovari_dla_biznesa_out': tovari_dla_biznesa_out,
                                                     'companies':set(companies),
                                                     'city': city,
                                                     'uslugi_dla_biznesa': uslugi_dla_biznesa,
                                                     'tovari_dla_biznesa': tovari_dla_biznesa
                                                     })

