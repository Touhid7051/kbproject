from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
import uuid


# Create your CustomUserManager here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, name, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            name = name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, name, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, first_name, last_name, name, password, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, name, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, first_name, last_name, name, **extra_fields)

# Creating User Model here.
class User(AbstractBaseUser,PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default,Custom model from nantu vai iplemented here.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    address = models.CharField( max_length=250)
    reset_password_token=models.CharField(max_length=200,null=True,blank=False)
    reset_password_sent_at = models.DateTimeField(auto_now_add=False,null=True)
    remember_created_at =  models.DateTimeField(auto_now_add=False,null=True)
    created_at =  models.DateTimeField(auto_now_add=False,null=True)
    updated_at =  models.DateTimeField(auto_now=False,null=True)
    sign_in_count=models.IntegerField(default=0)
    current_sign_in_at =  models.DateTimeField(auto_now=False,null=True)
    last_sign_in_at =  models.DateTimeField(auto_now=False,null=True)
    current_sign_in_ip = models.GenericIPAddressField(null=True)
    last_sign_in_ip =  models.GenericIPAddressField(null=True)
    affiliate_id = models.CharField(max_length=200,null=True,blank=True)
    phone_number = models.CharField(max_length=200,null=True,blank=True)
    confirmation_token = models.CharField(max_length=200,null=True,blank=True)
    confirmed_at = models.DateTimeField(auto_now_add=False,null=True)
    confirmation_sent_a = models.DateTimeField(auto_now_add=False,null=True)
    unconfirmed_emai = models.EmailField(null=True)
    failed_attempts = models.IntegerField(default=0)
    locked_at = models.DateTimeField(auto_now=False,null=True)
    email_confirmed = models.BooleanField(default = False,null = False,blank=False)
    unconfirmed_email_request = models.BooleanField(default = False,null = False,blank=False)
    kyc_status =  models.CharField(max_length=200,null=False,blank=False,default='not_completed')
    banned_reason =  models.CharField(max_length=200,null=True,blank=True)   
    banned = models.BooleanField(default = False,null = False,blank=False)
    kyc_status_reason = models.CharField(max_length=200,null=True,blank=True)
    affiliate_status = models.CharField(max_length=200,null=True,blank=True, default='not_completed')
    affiliate_formed_id = models.CharField(max_length=200,null=True,blank=True)
    kyc_status_by_id = models.UUIDField(default=uuid.uuid4)
    affiliate_status_by_id = models.UUIDField(default=uuid.uuid4)
    google_secret = models.CharField(max_length=50, null=True)
    google_mfa_activated = models.BooleanField(default = False,null = False,blank=False)
    deleted =  models.BooleanField(default = False,null = False,blank=False)
    kyc_confirmed_at = models.DateTimeField(auto_now=False,null=True)
    subscribed =  models.BooleanField(default = True,null = False,blank=False)
    role = models.IntegerField(default=0,null=False)
    sponsor = models.UUIDField(default=uuid.uuid4)
    users_status = models.CharField(max_length=200,null=True,blank=True)
    ref_id =  models.CharField(max_length=200,null=True,blank=True)



    #system predefined models
    is_staff = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(default=False) # this field we inherit from PermissionsMixin.
    

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'