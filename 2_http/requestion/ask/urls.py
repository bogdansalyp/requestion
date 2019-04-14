from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('hot/', views.hot, name='hot'),
    path('tag/<slug:tag_name>', views.tag, name='tag'),
    path('question/<int:question_id>', views.question, name='question'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('ask', views.ask, name='ask')
]