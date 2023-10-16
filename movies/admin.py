from django.contrib import admin
from movies.models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Movie._meta.fields]
    list_display_links = ['title']
    
admin.site.register(Movie, MovieAdmin)