from django.db import models

class Brand(models.Model):
    brand = models.CharField(max_length=200)

    class Meta:
        db_table = 'brand'

class Level(models.Model):
    level = models.CharField(max_length=100)

    class Meta:
        db_table = 'level'

class Products(models.Model):
    name             = models.CharField(max_length=45)
    category         = models.CharField(max_length=10, null=True)
    thumbnail        = models.CharField(max_length=300)
    heart_count      = models.IntegerField(default=0, null=True)
    like             = models.IntegerField(default=0, null=True)
    retail_price     = models.IntegerField(default=0, null=True)
    discount_percent = models.IntegerField(default=0, null=True)
    monthly_pay      = models.Intege'1rField(default=0, null=True)
    monthly_payment  = models.IntegerField(default=0, null=True)
    brand_id         = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    detail_category  = models.CharField(max_length=50, null=True)
    level_id         = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    cover_image      = models.CharField(max_length=100, null=True)
    end_datetime     = models.DateTimeField(null=True)
    status           = models.IntegerField(choices=((0, _("information")),
                                                    (1, _("title_cover")),
                                                    (2, _("introduction")),
                                            default=0)

    # creator          = models.ForeignKey(User, on_delete=models.CASCADE  유저앱 생성하면.
    
    class Meta:
        db_table = 'products'

class DetailImage(models.Model):
    name         = models.ForeignKey(Products, on_delete=models.CASCADE)
    detailImage  = models.CharField(max_length=300)
    
    class Meta:
        db_table = 'detailImage'

class Introduction(models.Model):
    name               = models.ForeignKey(Products, on_delete=models.CASCADE)
    introduction_image = models.CharField(max_length=500)
    introduction_text  = models.CharField(max_length=500)

    class Meta:
        db_table = 'introduction'
