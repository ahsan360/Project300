from django.urls import path
from django.contrib.auth import views as auth_views
#from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.hello,name='hello' ),
    path('hello/',views.hello,name='hello' ),
    path('index/',views.index,name='index' ),
    path('signin/',views.signin,name='signin' ),
    #path('log/',views.log,name='log' ),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('posts/', views.posts,name='posts'),
    path('cpost/', views.cpost,name='cpost'),
    path('search/', views.search,name='search'),
    path('<int:id>', views.details,name='details'),
    path('log/',auth_views.LoginView.as_view(template_name='projectApp/log.html'),name='login'),
    path('logo/',auth_views.LogoutView.as_view(template_name='projectApp/home.html'),name='logout')
] 