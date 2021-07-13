from django.urls import path
from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'
urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    # 클래스에는 .as_view 필요
    path('create/', AccountCreateView.as_view, name='create'),
]
