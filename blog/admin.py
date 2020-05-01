from django.contrib import admin
from .models import Post,Comment

# Register your models here.

# モデル登録
admin.site.register(Post)
# コメントモデルの登録
admin.site.register(Comment)