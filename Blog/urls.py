from . import views
from django.urls import path

urlpatterns = [
    path('',views.Home, name='home'),
    path('blog/<int:pk>', views.BlogDetail, name='blogdetail'),
    path('delete/<int:pk>', views.BlogDelete, name='blogdelete'),
    path('update/<int:pk>', views.BlogUpdate, name='blogupdate'),

]