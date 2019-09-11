# from django.db import models
# from django.db.models.deletion import ProtectedError
# from .utils import generate_unique_slug


# class ExcludeDeletedManager(models.Manager):
#     def get_queryset(self):
#         return super(ExcludeDeletedManager, self).get_queryset().filter(_deleted=False)


# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     _deleted = models.BooleanField(default=False)

#     objects = ExcludeDeletedManager()
#     admin_manager = models.Manager()

#     class Meta:
#         abstract = True
#         ordering = ['-created_at']

#     def delete(self, using=None):
#         try:
#             super(BaseModel, self).delete(using)
#         except ProtectedError:
#             self._deleted = True
#             self.save()


# class Person(BaseModel):
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     sex = models.CharField(max_length=1, choices=(('f', 'Femenino'), ('m', 'Masculino')))
#     birthday = models.DateField(null=True)
#     address = models.CharField(max_length=100, blank=True)
#     phone = models.CharField(max_length=100, blank=True)
#     country = models.CharField(max_length=100, blank=True)
#     province = models.CharField(max_length=100, blank=True)
#     city = models.CharField(max_length=100, blank=True)

#     class Meta:
#         abstract = True