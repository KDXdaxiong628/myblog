from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    # 发布日期
    # auto_now=True 在博客详情不能修改日期. 如果想要可以修改日期，可以改成 null=True  （一定要代码移植）
    pub_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title