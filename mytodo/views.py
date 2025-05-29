from django.shortcuts import render
from django.views import  View
from .models import Task

class IndexView(View):
    def get(self, request):
        # todoリストを取得
        todo_list = Task.objects.all()
        context = {"todo_list": todo_list}

        # テンプレートをレンダリング
        return render(request, "mytodo/index.html", context)

# ビュークラスをインスタンス化
index = IndexView.as_view()
