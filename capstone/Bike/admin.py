from django.contrib import admin
from Bike.models import Bike,Comparison,ServiceType,Maintenance
# Register your models here.

admin.site.register(Bike)
admin.site.register(Comparison)
admin.site.register(ServiceType)
admin.site.register(Maintenance)