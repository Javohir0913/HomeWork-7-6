from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"
        db_table = 'categories'


class Journal(models.Model):
    journal_title = models.CharField(max_length=255)
    journal_description = RichTextField()
    journal_image = models.ImageField(upload_to='journal/')
    journal_contact = RichTextField()
    journal_pub_date = models.DateTimeField(auto_now_add=True)
    journal_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    journal_author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.journal_title

    class Meta:
        verbose_name_plural = "Journals"
        db_table = 'journals'
