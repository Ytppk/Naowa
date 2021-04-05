from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']
    
    def __str__(self):
        return self.title


VAR_RANK = (
    ('Rank', 'Rank'),
    ('2nd Lt', '2nd Lt'),
    ('Lt', 'Lt'),
    ('Capt', 'Capt'),
    ('Maj', 'Maj'),
    ('Lt Col', 'Lt Col'),
    ('Col', 'Col'),
    ('Brig Gen', 'Brig Gen'),
    ('Maj Gen', 'Maj Gen')
)

class Members(models.Model):
    category = models.ForeignKey(Category, related_name='memberss', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    husbandname = models.CharField(max_length=255)
    rank = models.CharField(max_length=255, choices=VAR_RANK, default='Rank')
    appointment = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=600)
    dob = models.DateField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_added']
        unique_together = ('name', 'slug')

    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
