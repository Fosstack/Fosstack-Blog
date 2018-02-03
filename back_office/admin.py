from django.contrib import admin

from .models import Subscribe, Contact


class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Subscribe

    list_display = ['name', 'timestamp']


admin.site.register(Subscribe)
admin.site.register(Contact, ContactAdmin)
