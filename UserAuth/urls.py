from django.urls import path
from UserAuth import views

urlpatterns = [
    path('', views.signin,name='signin'),
    path('signup/', views.signup,name='signup'),
    path('home/<slug:username>', views.home,name='home'),
    path('logout/', views.signout,name='signout'),
]