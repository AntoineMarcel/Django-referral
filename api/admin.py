from django.contrib import admin
from .models import Parrain,Campaign,Steps

class MyModelAdmin(admin.ModelAdmin):
    readonly_fields=('userCode',)


class MyModel2Admin(admin.ModelAdmin):
    readonly_fields=('token',)


admin.site.register(Parrain, MyModelAdmin)
admin.site.register(Campaign, MyModel2Admin)
admin.site.register(Steps)
