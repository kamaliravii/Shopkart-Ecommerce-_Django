from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name="register"),
    path('collection/',views.collections,name="collections"),
    path('collection/<str:name>',views.collectionsView,name="collections"),
]