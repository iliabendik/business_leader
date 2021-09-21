from django.contrib import admin
from .models import Category
from .models import Company
from .models import City
from .models import Uslugi_dla_biznesa
from .models import Tovari_dla_biznesa
from .models import Investicii
from .models import Kommercheskie_tenderi
from .models import Meri_podderjki
from .models import Pervaya_socialnaya_birja
from .models import Socialnie_projekti




admin.site.register(Company)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Uslugi_dla_biznesa)
admin.site.register(Tovari_dla_biznesa)
admin.site.register(Investicii)
admin.site.register(Kommercheskie_tenderi)
admin.site.register(Meri_podderjki)
admin.site.register(Pervaya_socialnaya_birja)
admin.site.register(Socialnie_projekti)
