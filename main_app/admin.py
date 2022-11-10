from django.contrib import admin
from .models import Elephant, Feeding, Toy, Photo

admin.site.register(Elephant)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)