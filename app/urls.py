from django.urls import path

from .views import addtekstitietokantaan, indexview, tekstipuhdistusview, deleteteksti, confirmdelete, addtekstitietokantaan, tekstialkuperainen_get,tietokantalistview


urlpatterns = [
    path('', indexview),
    path('tekstipuhdistus/', tekstipuhdistusview),
    path('tekstialkuperainen_get/',tekstialkuperainen_get),
    path('tietokanta/', tietokantalistview),
    path('lisaa-tietokantaan/', addtekstitietokantaan),
    # path('editsivulle/',editsivulle),
    path('confirm-delete/<int:id>/', confirmdelete),
    path('deleteteksti/<int:id>/', deleteteksti),
]