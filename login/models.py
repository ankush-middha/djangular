import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


def get_profile_image_path(instance, filename):
    return os.path.join('profile_%d'%(instance.id), filename)


class User(AbstractBaseUser, PermissionsMixin):
    '''
    User model class inherited from AbstractBaseUser
    '''
    GENDER_CHOICES = (
        ('Male','M'),
        ('Female','F')
    )
    username = models.CharField(_('User Name'), max_length=50, null=True)
    email = models.EmailField(_('Email'),unique=True)
    gender = models.CharField(_('Gender'), choices= GENDER_CHOICES, null=True, blank=True, max_length=20)
    contact_no = models.CharField(_('Phone'), max_length=20, null=True, blank=True)
    profile_pic = models.ImageField(upload_to=get_profile_image_path, max_length=500, null=True, blank=True)
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Staff Status'), default=False)
    # video = models.FileField(_('video'), null=True, blank=True, upload_to=get_profile_image_path)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]
    objects = UserManager()

    def __unicode__(self):
        return self.email

    def get_short_name(self):
        return self.username
