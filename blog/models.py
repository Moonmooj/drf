from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField('카테고리 이름', max_length=50)
    description = models.TextField('설명')


    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField('제목', max_length=50)
    category = models.ManyToManyField(Category, verbose_name='카테고리')
    contents = models.TextField('내용')
    exposure_start_date = models.DateField('노출 시작 일자',default=timezone.now())
    exposure_end_date = models.DateField('노출 시작 일자',default=timezone.now())

    def __str__(self):
        return f"{self.author.username} 님이 작성하신 글입니다."

class Comment(models.Model):
    user = models.ForeignKey('user.User', verbose_name="사용자", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name="게시글", on_delete=models.CASCADE)
    contents = models.TextField("내용")

    def __str__(self):
       return f"{self.user.username} 님이 작성하신 글입니다."

