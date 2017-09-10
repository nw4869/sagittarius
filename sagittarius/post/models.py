from django.db import models


class PublicPostManager(models.Manager):
    def get_queryset(self):
        return super(PublicPostManager, self).get_queryset().filter(private=True)


class Post(models.Model):
    title = models.CharField('标题', max_length=85)
    content = models.TextField('内容')

    private = models.BooleanField('私密', default=False)

    created = models.DateField('创建时间', auto_now_add=True)
    updated = models.DateField('更新时间', auto_now=True)

    public = PublicPostManager()

    def __str__(self):
        return '{}: {}'.format(self.title, self.content[:10] if self.content else None)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
