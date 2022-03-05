from django.contrib import admin
from .models import Category, Game, GameSearch, Membership, UserMembership, Subscription, FreeGame


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class FreeGameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(UserMembership)
admin.site.register(Membership)
admin.site.register(Subscription)

admin.site.register(Category, CategoryAdmin)
admin.site.register(FreeGame, FreeGameAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GameSearch)



