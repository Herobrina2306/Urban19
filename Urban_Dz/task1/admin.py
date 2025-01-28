from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    search_fields = ('title',)
    list_filter = ('size', 'cost')
    list_per_page = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balanse', 'age')
    search_fields = ('name', )
    list_filter = ('balanse', 'age')
    readonly_fields = ('balanse',)
    list_per_page = 30

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_filter = ('date', )
