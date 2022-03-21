from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from insert import views

urlpatterns = [  
    path('', views.index),  
    path('show/',views.show,name ="show"), 
    path('img', views.img,name="img"),  
    path('edit/<int:id>', views.edit),  
    path('update_data/<int:id>', views.update_data),  
    path('delete/<int:id>', views.destroy),
    
    path('item/', views.item, name="item"),
     
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)