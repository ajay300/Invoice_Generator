# from django.contrib import admin
from django.urls import path 
from . import views
# from testapi  import views 
urlpatterns = [

    #---------------------------------------------Combo Concrete View---------------------------------------

    #product api
    path('productview/',views.ProductListcreate.as_view()),
    path('productadd/<int:pk>/',views.ProductRetrieveUpdate.as_view()),
    path('productremove/<int:pk>',views.ProductRetrieveDestroy.as_view()),
    

    #customer api

    path('customerview/',views.CustomerListcreate.as_view()),
    path('customeradd/<int:pk>/',views.CustomerRetrieveUpdate.as_view()),
    path('customerremove/<int:pk>',views.CustomerRetrieveDestroy.as_view()),
    


    # --------------------------modelmixin + genericView------------------------------

    # path('productlapi/',views.ProductList.as_view()),
    # path('productapipost/',views.Productcreate.as_view()),
    # path('productapi/<int:pk>',views.ProductRetrieve.as_view()),
    # path('productapi/<int:pk>/',views.ProductUdpate.as_view()),
    # path('productapikill/<int:pk>/',views.ProductDestroy.as_view()),
        
    

]
