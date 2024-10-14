from django.contrib import admin

# Register your models here.
from .models import  Author1
from .models import Destinations
from .models import  Item

admin.site.register(Item)

# admin.site.register(Author1)
admin.site.register(Destinations)

class AuthorAdmin(admin.ModelAdmin):
    list_display=('author_name','book_name')
    search_fields = ('author_name',)

admin.site.register(Author1,AuthorAdmin)

