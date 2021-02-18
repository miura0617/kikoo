from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post


# Create your views here.

class PostLisView(ListView):
    model = Post
    template_name = "tweet/index.html"
    context_object_name = 'posts'     # Djangoがテンプレートファイルで使える変数としてobject_listか<モデル名>_listのどちらかで扱えるように自動生成するが、名前を決めることもできる
    ordering = ['-date_post']         # 表示する順番を決める。最新投稿から表示したいので'-'を付けて、モデルのdate_posted変数の日付順
    paginate_by = 5                   # １ページに何個表示するかという設定

class PostCreateView(CreateView):
    model = Post
    fields = ['content']              # 投稿するときにmodelの何を使うか
    template_name = "tweet/post_create.html"
    success_url = '/'                 # 投稿が完了したらどこに戻るか