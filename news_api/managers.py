from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, username, avatar=None):
        """
        Create and save a user with the given email and password.
        """
        if None in (email, password, username):
            raise ValueError(_("Something was forgotten"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, avatar=avatar)
        user.set_password(password)
        user.save()
        return user
