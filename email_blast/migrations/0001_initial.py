# Generated by Django 2.2 on 2019-04-01 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailBlast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='件名')),
                ('recipients', models.TextField(verbose_name='受取人のメールアドレス')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='書き時間')),
                ('last_updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新時間')),
                ('sent_at', models.DateTimeField(default=None, null=True, verbose_name='送り時間')),
                ('is_admin', models.BooleanField(default=False, verbose_name='管理\x1f者向き')),
                ('sent', models.BooleanField(default=False, verbose_name='送った')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='送り人')),
            ],
            options={
                'ordering': ['-last_updated_at', '-created_at', '-sent_at'],
            },
        ),
    ]