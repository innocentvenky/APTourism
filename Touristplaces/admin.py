from django.contrib import admin
from Touristplaces.models import aboutap,aboutimages
from Touristplaces.models import place1,place1images,place1video
from Touristplaces.models import place2,place2images,place2video

# Register your models here.
class aboutadmin(admin.ModelAdmin):
    list_d=['id','apabout','aboutminister','image']
admin.site.register(aboutap,aboutadmin)
admin.site.register(aboutimages)
admin.site.register(place1)
admin.site.register(place1images)
admin.site.register(place1video)
admin.site.register(place2)
admin.site.register(place2images)
admin.site.register(place2video)
