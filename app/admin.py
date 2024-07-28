from django.contrib import admin
from .models import Player, Team, MyTeam, Match
# Register your models here.


class PlayerAdmin(admin.ModelAdmin):
    list_per_page: int = 15
    search_fields = ('name',)
 
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_date', 'show_match')
    list_filter = ('match_date', 'team_a', 'team_b')
     #Nome do relacionamento, dois anderscores para indicar qual é o campo. São chamados de Lookup 
     #O Filtro funciona para o time A e Time B
    search_fields = ('team_a__name', 'team_b__name') # team_b__icontains__name
    
    def show_match(self, obj):
        return f'{obj.team_a} {obj.team_a_goal} x {obj.team_b} {obj.team_b_goal}'
    
    show_match.short_description = 'Jogo'
    
admin.site.register(Player, PlayerAdmin)
admin.site.register(Team)
admin.site.register(MyTeam)
admin.site.register(Match, MatchAdmin)
