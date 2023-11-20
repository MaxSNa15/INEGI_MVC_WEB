from django.contrib import admin
from .models import Municipality, Locality, Residence, Resident, EconomicActivity

class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'population')
    search_fields = ('name', 'region', 'population')

class LocalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'municipality')
    search_fields = ('name', 'municipality')

class ResidenceAdmin(admin.ModelAdmin):
    list_display = ('adress', 'type_of_residence', 'locality')
    search_fields = ('adress', 'type_of_residence', 'locality')

class ResidentAdmin(admin.ModelAdmin):
    list_display = ('first_name' , 'last_name', 'gender')
    search_fields = ('first_name' , 'last_name', 'gender')

class EconomicActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


# Register your models in the admin site
admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(Residence, ResidenceAdmin)
admin.site.register(Resident, ResidentAdmin)
admin.site.register(EconomicActivity, EconomicActivityAdmin)
