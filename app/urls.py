from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),
    # path('pff/',views.pdfj, name = 'pdfj'),
    path('buy/<int:pk>/',views.buy,name='buy'),
    path('pdf/',views.pdf,name='pdf'),


    path('login/',views.loginPage , name = "login"),
    path('register/',views.registerPage , name = "register"),
    path('logout/',views.logoutUser, name = "logout"),

]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
