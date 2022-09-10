from django.contrib import admin
from .models import *


admin.site.register(CategoryModel)

class CaseImagesModelAdmin(admin.StackedInline):
    model = CaseImagesModel

class CaseModelAdmin(admin.ModelAdmin):
    # list_display = ["name", "price", "duration", "location"]
    inlines = [CaseImagesModelAdmin]
    class Meta:
        model = GeneralCaseModel

admin.site.register(GeneralCaseModel, CaseModelAdmin)
