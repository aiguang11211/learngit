 # -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .conf import settings
from .managers import UserInheritanceManager, UserManager

from datetime import datetime
import json,time

	
	
class AbstractUser(AbstractBaseUser, PermissionsMixin):
    USERS_AUTO_ACTIVATE = not settings.USERS_VERIFY_EMAIL

    email = models.EmailField(
        _('email address'), max_length=255, unique=True, db_index=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))

    is_active = models.BooleanField(
        _('active'), default=USERS_AUTO_ACTIVATE,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    user_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, editable=False)

    objects = UserInheritanceManager()
    base_objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        abstract = True

    def get_full_name(self):
        """ Return the email."""
        return self.email

    def get_short_name(self):
        """ Return the email."""
        return self.email

    def email_user(self, subject, message, from_email=None):
        """ Send an email to this User."""
        send_mail(subject, message, from_email, [self.email])

    def activate(self):
        self.is_active = True
        self.save()

    def save(self, *args, **kwargs):
        if not self.user_type_id:
            self.user_type = ContentType.objects.get_for_model(self, for_concrete_model=False)
        super(AbstractUser, self).save(*args, **kwargs)


class User(AbstractUser):

    """
    Concrete class of AbstractUser.
    Use this if you don't need to extend User.
    """
    name=models.CharField(max_length=20,default='未设置')
    sex=models.CharField(max_length=3,default='未设置')

    job_number=models.CharField(max_length=10,default='未设置')
    
    zhengzhi_miaomao=models.CharField(max_length=10,default='未设置')
    zhengzhi_time=models.CharField(max_length=20,default='未设置')
    
    job=models.CharField(max_length=30,default='未设置')
    job_time=models.CharField(max_length=20,default='未设置')
    job_2=models.CharField(max_length=30,default='未设置')
    id_number=models.CharField(max_length=30,default='未设置')
    xue_li=models.CharField(max_length=30,default='未设置')
    school=models.CharField(max_length=30,default='未设置')
    graduate_time=models.CharField(max_length=20,default='未设置')
    job_join_time=models.CharField(max_length=20,default='未设置')
    team_belong=models.CharField(max_length=20,default='未设置')
    phone=models.CharField(max_length=30,default='未设置')

    def __str__(self):
        return self.name

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
