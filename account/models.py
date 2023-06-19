from django.db import models
from django.contrib.auth.models import User
import datetime, os

from django.dispatch import receiver
####=====================custom user model=======================
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser, Group
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, email,password=None, **kwargs):
        if not username:
            raise ValueError('Accounts must have a  username')
        if not email:
            raise ValueError('Accounts must have a  email')
        if not password:
            raise ValueError('Accounts must have a  password')
        user = self.model(username=username, email=email)
        self.password = make_password(password)
        user.set_password(self.password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email,password):
        user = self.model(email=email, password=make_password(password),
                          username=username, )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(verbose_name='first name', max_length=255)
    last_name = models.CharField(verbose_name='last name', max_length=255)
    g = (('Male', 'Male'),
         ('Female', 'Female'),)
    gender = models.CharField(choices=g, default='Male', verbose_name='Gender', max_length=255)
    phone_num = models.CharField(verbose_name='Phone number', max_length=14, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, )
    country = models.CharField(verbose_name='country', max_length=14, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
