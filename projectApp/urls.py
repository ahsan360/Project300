from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
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
    path('Update/<int:pk>', views.Update,name='Update'),
    path('delete/<int:pk>', views.delete,name='delete'),
    path('delete_comment/<int:pk>', views.delete_comment,name='delete_comment'),
    path('comment/<int:pk>', views.addcomment,name='addcomment'),
    path('log/',auth_views.LoginView.as_view(template_name='projectApp/log.html'),name='login'),
    path('logo/',auth_views.LogoutView.as_view(template_name='projectApp/home.html'),name='logout')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 