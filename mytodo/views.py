from django.shortcuts import redirect, render
from django.views import  View

from mytodo.forms import TaskForm
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

class AddView(View):
    def get(self, request):
        # 空のフォームを作ってテンプレートに渡す
        form = TaskForm()
        # テンプレートのレンダリング処理
        return render(request, "mytodo/add.html", {'form': form})

    def post(self, request, *args, **kwargs):
        # 登録処理
        # 入力データをフォームに渡す
        form = TaskForm(request.POST)
        # 入力データに誤りがないかチェック
        is_valid = form.is_valid()

        # データが正常であれば
        if is_valid:
            # モデルに登録
            form.save()
            return redirect('/')

        # データが正常じゃない
        return render(request, 'mytodo/add.html', {'form': form})
                      
add = AddView.as_view()

class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')

        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()

        return redirect('/')
    
update_task_complete = Update_task_complete.as_view()