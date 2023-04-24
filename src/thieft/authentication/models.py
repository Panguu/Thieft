from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.crypto import get_random_string
import uuid

class UserProfile(models.Model):
    id=models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=128, null=True, blank=True)
    lastName = models.CharField(max_length=128, null=True, blank=True)
    phoneNumber = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    country = models.CharField(max_length=128, null=True, blank=True)

class UserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError('Users must have a username')
        
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_profile():
        profile = UserProfile()
        profile.save()
        return profile

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user
    def change_password(self, username, password):
        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def change_username(self, username, new_username):
        user = self.model(
            username=username,
        )

        user.set_username(new_username)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=255, unique=True)
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def has_perm(self, perm, obj=None):
        
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    def __str__(self):
        return self.username

