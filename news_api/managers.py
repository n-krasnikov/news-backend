from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, username, email, password, avatar=None):
        if not username:
            raise TypeError('Users must have a username.')

        if not email:
            raise TypeError('Users must have an email address.')
        
        if not password:
            raise TypeError('Users must have a passwords.')

        email=self.normalize_email(email)
        user = self.model(email=email, username=username, avatar=avatar)
        user.set_password(password)
        user.save()

        return user