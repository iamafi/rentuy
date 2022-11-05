from django.contrib import admin

from property.models import Property, PropertyImage, PropertyVideo


class PropertyImageAdmin(admin.StackedInline):
    model = PropertyImage
    min_num = 1
    max_num = 10


class PropertyVideoAdmin(admin.StackedInline):
    model = PropertyVideo
    min_num = 1
    max_num = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'district')
    list_filter = ('owner', 'district',)
    inlines = [PropertyImageAdmin, PropertyVideoAdmin]
