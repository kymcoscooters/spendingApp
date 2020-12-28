from django.urls import path

from . import views

app_name = 'spending'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('postlogin', views.postlogin, name='postlogin'),
    path('createUser', views.CreateUserView.as_view(), name='createUser'),
    path('postCreateUser', views.postCreateUser, name='postCreateUser'),
    path('user/<int:pk>', views.UserView.as_view(), name='user'),
    path('addReceipt/<int:user_id>', views.createReceipt, name='createReceipt'),
    path('postCreateReceipt/<int:user_id>', views.postCreateReceipt, name='postCreateReceipt'),
    path('addStyle/<int:user_id>', views.addStyle, name='addStyle')
]