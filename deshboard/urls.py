from django.urls import path
from . import views


urlpatterns = [
    
   path('',views.index, name='index'),
   path('senddata/', views.senddata, name='index'),
   path('data/', views.data, name='data'),
   path('delete/<int:id>',views.delete, name='delete' ),
   path('edit/<int:id>',views.edit, name='edit' ),
   path('update/',views.update,name='update'),
   path('details/<slug>',views.details,name='update'),
   path('blog/',views.blog,name='update'),


]