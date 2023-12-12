from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
      path('',views.home,name="home"),
      path('signin',views.signin,name="signin"),
      path('signup',views.signup,name="signup"),
      path('logout',views.user_logout,name="logout"),
      path('topic',views.home2,name="home2"),
      path('basicsyntax',views.basicsyntax,name='basicsyntax'),
      path('topic/quiz',views.temp,name='temp'),
      path('dbtopic',views.home3,name="home3"),

      path('dbtopic/quiz',views.quiz,name="quiz"),

      path('dbtopic/week1',views.dbbasic,name="dbbasic"),
      path('topic/practice',views.practice,name='practice'),
      path('topic/practice/coding',views.code,name="code"),
      path('python',views.python,name='python'),
      path('python/week1',views.pcontent,name="pcontent"),
      path('python/quiz',views.pquiz,name='pquiz'),
      path('python/pquiz',views.pquiz,name='pquiz'),
      
]