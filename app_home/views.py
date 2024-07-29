from django.shortcuts import render
from .models import Player

# Create your views here.

#Django - Model Views Controller
            #Views = Template
            #Controller = Views
# No geral MVT Django é mais um , Model View Template

# @login_required(login_url='/login/')
def show_players(request):
    players = Player.objects.all() #QuerySet - Lista de objetos do tipo Player
    return render(request,'app/show_players.html', {'players': players}) 


# Retorno como API
# Recomendado usar o DJANGO-REST-FRAMEWORK
def endpoints(request):
    return JsonResponse({'message':'Hello World'})

##### ---- AULA SOBRE ALLAUTH AND HTMX

def home_view(request):
    return render(request,'app/home.html')