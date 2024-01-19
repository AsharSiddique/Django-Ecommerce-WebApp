from django.contrib.auth.backends import ModelBackend
from .models import Customers

class EmailBackend(ModelBackend):
    def authenticate(self, request, cemail=None, cpassword=None, **kwargs):
        try:
            user = Customers.objects.get(cemail=cemail,  cpassword=cpassword)
        except Customers.DoesNotExist:
            return None
        else:
            return user