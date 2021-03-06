# Generated by Django 2.0.5 on 2018-07-17 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_pk', models.AutoField(primary_key=True, serialize=False)),
                ('marksmemo', models.FileField(blank=True, null=True, upload_to='documentapp.DocumentMarksmemo/bytes/filename/mimetype')),
                ('aadharcard', models.FileField(blank=True, null=True, upload_to='documentapp.Documentaadharmemo/bytes/filename/mimetype')),
                ('projectfile', models.FileField(blank=True, null=True, upload_to='documentapp.Documentprojectmemo/bytes/filename/mimetype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documentaadharmemo',
            fields=[
                ('book_cover_pk', models.AutoField(primary_key=True, serialize=False)),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=500)),
                ('mimetype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentMarksmemo',
            fields=[
                ('book_cover_pk', models.AutoField(primary_key=True, serialize=False)),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=500)),
                ('mimetype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Documentprojectmemo',
            fields=[
                ('book_cover_pk', models.AutoField(primary_key=True, serialize=False)),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=500)),
                ('mimetype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pic', models.ImageField(blank=True, default='default.jpg', upload_to='documentapp.Profilepath/bytes/filename/mimetype', verbose_name='Current pic')),
                ('city', models.CharField(blank=True, default='', max_length=25)),
                ('address', models.TextField(verbose_name='location')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profilepath',
            fields=[
                ('profile_cover_pk', models.AutoField(primary_key=True, serialize=False)),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=255)),
                ('mimetype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SingleDocument',
            fields=[
                ('document_pk', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(default='Marksmemo', max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='documentapp.SingleDocumentStorage/bytes/filename/mimetype')),
                ('visible', models.IntegerField(default=0, verbose_name='0:not visible ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SingleDocumentStorage',
            fields=[
                ('book_cover_pk', models.AutoField(primary_key=True, serialize=False)),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=500)),
                ('mimetype', models.CharField(max_length=100)),
            ],
        ),
    ]
