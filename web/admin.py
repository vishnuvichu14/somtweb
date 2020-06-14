from django.contrib import admin
from .models import Cow,Milk,Worker,Farm,Breed

admin.site.register(Cow)
admin.site.register(Milk)
admin.site.register(Farm)
admin.site.register(Worker)
admin.site.register(Breed)

