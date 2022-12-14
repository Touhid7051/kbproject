# Generated by Django 4.1 on 2022-08-10 06:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20220809_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='affiliate_formed_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='affiliate_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='affiliate_status',
            field=models.CharField(blank=True, default='not_completed', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='affiliate_status_by_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='user',
            name='banned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='banned_reason',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='confirmation_sent_a',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='confirmation_token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='confirmed_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='current_sign_in_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='current_sign_in_ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='failed_attempts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='google_mfa_activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='google_secret',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='kyc_confirmed_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='kyc_status',
            field=models.CharField(default='not_completed', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='kyc_status_by_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='user',
            name='kyc_status_reason',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_sign_in_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_sign_in_ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='locked_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ref_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='remember_created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='reset_password_sent_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='reset_password_token',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='sign_in_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='sponsor',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='user',
            name='subscribed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='unconfirmed_emai',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='unconfirmed_email_request',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='users_status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
