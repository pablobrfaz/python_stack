from django.db import models



# Create your models here.
class CursoManager(models.Manager):
    def curso_validator(self, postData):
        errors = {}
        if len(postData['nombre'])<5:
            errors['nombre'] = "El nombre debe tener mas de 5 caracteres"
        if len(postData['description'])<10:
            errors['description'] = "La descripcion debe ser mayor a 15 caracteres"
        return errors


class curso(models.Model):
    nombre = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = CursoManager()

class description(models.Model):
    description = models.TextField()
    Curso = models.OneToOneField(curso, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
