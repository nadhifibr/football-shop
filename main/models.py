import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Football'),
        ('accessories', 'Accessories'),
        ('training', 'Training Equipment'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0,
        validators=[
            MinValueValidator(0.0),   
            MaxValueValidator(5.0)    
        ]
    )

    def __str__(self):
        return self.title
    
    @property
    def is_in_stock(self):
        return self.stock > 0
    