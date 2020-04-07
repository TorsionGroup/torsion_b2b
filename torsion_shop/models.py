from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField("Brand", max_length=250)
    enabled = models.IntegerField()
    source_id = models.(max_length=250)
    wait_list = models.IntegerField()
    is_recommended = models.IntegerField()
    sort_index = models.IntegerField()
    source_type = models.(max_length=250)
    gallery_attribute = models.(max_length=250)
    gallery_name = models.(max_length=250)
    kind = models.(max_length=250)
    description = models.TextField("Description")
    url = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"