from django.urls import path
from . import views
urlpatterns = [
    path("",views.tax1,name="tax"),
    path("<int:num>",views.tax2,name="num"),
    path("taxrate", views.tax3, name="rate")
    ]
