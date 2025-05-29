from django.shortcuts import render
from django.views import  View

class IndexView(View):
    def get(self, request):
        # todoリスト取得

        # テンプレートをレンダリング
        return render(request, "mytodo/index.html")

# ビュークラスをインスタンス化
index = IndexView.as_view()
