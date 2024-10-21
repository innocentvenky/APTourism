from django.urls import path
from . import views
urlpatterns = [
       path('',views.welcome),
       path('main/',views.main),
       path('about/',views.about),
       path('place1/',views.tplace1),
       path('place2/',views.tplace2),
       path('aboutme/',views.aboutme),

]
