from django.contrib import admin
from .forms import *

class FAQAdmin(admin.ModelAdmin):
    list_filter = ('course',)  
    list_display = ('question', 'course')
class EnquiryFormAdmin(admin.ModelAdmin):
    form = EnqForm
    list_display = ('name', 'email' , 'phone' ,'message','states' ,'created_at')
    search_fields =('name' , 'email' , 'phone' , 'states' )


from .models import *
admin.site.register(Banners)
admin.site.register(Facility)
admin.site.register(home_page_data)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(EnquiryForm)