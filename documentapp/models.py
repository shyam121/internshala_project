from django.db import models
from django.contrib.auth.models import User
from db_file_storage.model_utils import delete_file, delete_file_if_needed
from db_file_storage.compat import reverse

from django.db.models.signals import post_save

# Create your models here.
class DocumentMarksmemo(models.Model):
    book_cover_pk = models.AutoField(primary_key=True)
    bytes = models.TextField()
    filename = models.CharField(max_length=500)
    mimetype = models.CharField(max_length=100)

class Documentaadharmemo(models.Model):
    book_cover_pk = models.AutoField(primary_key=True)
    bytes = models.TextField()
    filename = models.CharField(max_length=500)
    mimetype = models.CharField(max_length=100)

class Documentprojectmemo(models.Model):
    book_cover_pk = models.AutoField(primary_key=True)
    bytes = models.TextField()
    filename = models.CharField(max_length=500)
    mimetype = models.CharField(max_length=100)

class Document(models.Model):
    document_pk=models.AutoField(primary_key=True)
    marksmemo = models.FileField(
        upload_to='documentapp.DocumentMarksmemo/bytes/filename/mimetype',
        blank=True, null=True
    )
    aadharcard = models.FileField(
        upload_to='documentapp.Documentaadharmemo/bytes/filename/mimetype',
        blank=True, null=True
    )
    projectfile = models.FileField(
        upload_to='documentapp.Documentprojectmemo/bytes/filename/mimetype',
        blank=True, null=True
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url_edit(self):
        return reverse('documentapp:details.edit', kwargs={'pk': self.pk})

    def get_absolute_url_delete(self):
        return reverse('documentapp:details.delete', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        delete_file_if_needed(self, 'marksmemo')
        delete_file_if_needed(self, 'aadharcard')
        delete_file_if_needed(self, 'projectfile')
        super(Document, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Document, self).delete(*args, **kwargs)
        delete_file(self, 'marksmemo')
        delete_file(self, 'aadharcard')
        delete_file(self, 'projectfile')



class SingleDocumentStorage(models.Model):
    book_cover_pk = models.AutoField(primary_key=True)
    bytes = models.TextField()
    filename = models.CharField(max_length=500)
    mimetype = models.CharField(max_length=100)

class SingleDocument(models.Model):
    document_pk=models.AutoField(primary_key=True)
    file = models.FileField(
        upload_to='documentapp.SingleDocumentStorage/bytes/filename/mimetype',
        blank=True, null=True
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url_edit(self):
        return reverse('documentapp:details.edit', kwargs={'pk': self.pk})

    def get_absolute_url_delete(self):
        return reverse('documentapp:details.delete', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        delete_file_if_needed(self, 'file')
        super(SingleDocument, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(SingleDocument, self).delete(*args, **kwargs)
        delete_file(self, 'file')





class Profilepath(models.Model):
    profile_cover_pk = models.AutoField(primary_key=True)
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)

from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_pic = models.ImageField("Current pic",blank=True, upload_to="documentapp.Profilepath/bytes/filename/mimetype",default="default.jpg")
    # phonenum = PhoneNumberField()
    city=models.CharField(max_length=25, blank=True,default="")
    address=models.TextField('location')

def create_profile(sender, **kwargs):
    if kwargs['created']:
         user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)