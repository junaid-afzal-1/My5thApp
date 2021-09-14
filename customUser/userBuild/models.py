from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.


class MyUserManager(BaseUserManager):


    def create_user(self, username, password=None):

        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user




    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    profile_photo = models.ImageField()
    username = models.CharField(max_length=30,unique=True)

    USERNAME_FIELD = 'username'

    objects = MyUserManager()



