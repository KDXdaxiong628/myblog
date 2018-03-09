from django.contrib import admin

from .models import Article

# 配置Admin  ---- 根据自己需求，后天显示博客哪些内容

class AtricleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')

    # 添加admin过滤器  记住只有一个参数的时候要加 逗号 ,
    list_filter = ('pub_time',)

admin.site.register(Article, AtricleAdmin)
