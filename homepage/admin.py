from django.contrib import admin


class FAQAdmin(admin.ModelAdmin):
    list_filter = ('course',)  
    list_display = ('question', 'course')
    
from .models import *
admin.site.register(Banners)
admin.site.register(Facility)
admin.site.register(home_page_data)
admin.site.register(FAQ, FAQAdmin)