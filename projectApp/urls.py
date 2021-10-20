from django.urls import path
#from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.hello,name='hello' ),
    path('hello/',views.hello,name='hello' ),
    path('index/',views.index,name='index' ),
    path('signin/',views.signin,name='signin' ),
    path('login/',views.login,name='login' ),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('posts/', views.posts,name='posts'),
    path('cpost/', views.cpost,name='cpost'),
] 