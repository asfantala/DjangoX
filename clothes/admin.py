from django.contrib import admin
from .models import Clothing

class CustomClothingAdmin(admin.ModelAdmin):
    model = Clothing
    list_display = ['name', 'purchaser', 'price', 'size', 'color', 'description']
    fieldsets = (
        (
            Clothing,
            {
                'fields': ('name', 'purchaser', 'price', 'size', 'color', 'description'),
            },
        ),
    )

admin.site.register(Clothing, CustomClothingAdmin)
