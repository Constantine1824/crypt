from django.urls import path
from .views import index,Login,signUp

urlpatterns = [
    path('',index,name='index'),
    path('login',Login, name='login'),
    path('signup',signUp,name='signup'),
    # path('add',add,name='addPassword'),
    # path('view',viewPass,name='viewPass')
]