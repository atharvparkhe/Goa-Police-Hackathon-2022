from django.contrib import admin
from .models import *


admin.site.register(CategoryModel)

class CaseImagesModelAdmin(admin.StackedInline):
    model = CaseImagesModel

class CaseModelAdmin(admin.ModelAdmin):
    inlines = [CaseImagesModelAdmin]
    class Meta:
        model = CaseModel

admin.site.register(CaseModel, CaseModelAdmin)
