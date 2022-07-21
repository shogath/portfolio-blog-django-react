from django.contrib import admin

from .models import PortfolioProject, Contact

# Register your models here.


class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(PortfolioProject, PortfolioProjectAdmin)
admin.site.register(Contact)
