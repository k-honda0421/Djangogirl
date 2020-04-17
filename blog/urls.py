from django.urls import path
from . import views

# post_list という名前の ビュー をルートURLに割り当てる
urlpatterns = [
    path('',views.post_list,name='post_list'),
]