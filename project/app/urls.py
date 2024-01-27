from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('',views.home,name='home'),
    path('v/',views.home2,name="home2"),
    path('add/',views.add,name='add'),
    path('admim/',views.addim,name="addim"),
    path('admv/',views.addv,name="addv"),
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('delete_video/<int:video_id>/', views.delete_video, name='delete_video'),
]