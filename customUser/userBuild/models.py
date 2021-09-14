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

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = MyUserManager()



    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True



