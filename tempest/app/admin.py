from django.contrib import admin
from .models import SubstituicaoAula

from .models import Representante
from .models import Curso
# Register your models here.

admin.site.register(SubstituicaoAula)
admin.site.register(Representante)
admin.site.register(Curso)

