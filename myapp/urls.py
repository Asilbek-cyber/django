from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.main,name="hello my world"),
    path('about/',views.main1,name="hello my world"),
    path('amongus/',views.main2,name="hello my world"),
]
