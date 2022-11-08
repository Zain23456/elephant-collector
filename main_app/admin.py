from django.contrib import admin
from .models import Elephant, Feeding, Toy
# Register your models here.
admin.site.register(Elephant)
admin.site.register(Feeding)
admin.site.register(Toy)