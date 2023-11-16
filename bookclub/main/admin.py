from django.contrib import admin
from .models import *


class RoomsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

admin.site.register(Rooms, RoomsAdmin)

class BooksAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'genre',
        'pages',
        'room'
    ]

admin.site.register(Books, BooksAdmin)