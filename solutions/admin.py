from django.contrib import admin
from .models import Services, Solutions

class SolutionsAdmin(admin.ModelAdmin):
    list_display = ("solutions_name", "homepage")
    list_editable = ("homepage",)


admin.site.register(Solutions,SolutionsAdmin)
admin.site.register(Services)
