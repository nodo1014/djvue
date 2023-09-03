from django.db import models


# Post, Category, Tag, Comment
class Post(models.Model):
    # 테이블 관계부터 정의
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    # 필드
    # CharField 는  blank=True 만. null=Ture는 안좋아. 왜? null 이면, null 아 아니라 엠프티 스트링이 저장되게 하기위해
    title = models.CharField('제목', max_length=50)
    description = models.CharField('본문', max_length=100, blank=True, help_text='simple one-line text')
    image = models.ImageField('이미지', upload_to='blog/%Y/%m/', blank=True, null=True)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    like = models.PositiveSmallIntegerField('좋아요', default=0)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True, help_text='simple one-line text')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField('컨텐트')
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    @property
    def short_content(self):
        return self.content[:10]

    def __str__(self):
        return self.short_content
