from django.contrib import admin
from ranking.models import Ranking

class MovieAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ranking._meta.fields]
    list_display_links = ['user']
    
admin.site.register(Ranking, MovieAdmin)