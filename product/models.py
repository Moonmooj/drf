from django.db import models
import datetime

# Create your models here.


class Product(models.Model):
    author = models.ForeignKey('user.User', verbose_name='작성자', on_delete=models.CASCADE)
    title = models.CharField('제목',max_length=50)
    thumbnail = models.FileField('썸네일', upload_to="product/")
    description = models.TextField('설명', max_length=100)
    create_date = models.DateTimeField('등록일자', auto_now_add=True)
    post_start_date = models.DateField('노출시작일자')
    post_end_date = models.DateField('노출종료일자')
    is_active = True
    def __str__(self):
        return f"{self.author.username} 님이 올리신 제품입니다."

