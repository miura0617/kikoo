from django.db import models
from django.utils import timezone   # timezoneを使う
from django.contrib.auth.models import User # Userを使う

# Create your models here.

# 投稿するモデルを作成
class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)    # 一人の著者で複数POSTできるようにする(many-to-one field)
    date_post = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    # 投稿一覧に表示される表示名をcontentに設定
    def __str__(self):
        return self.content[:30]       # 投稿内容の先頭30文字を表示
