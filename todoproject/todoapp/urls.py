
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path("about/",views.about,name="about"),
    path("Create/",views.create,name="create"),
    path("Listeler/",views.listeler,name="listeler"),
    path("Delete/<Todo_id>", views.delete, name="delete")

]


