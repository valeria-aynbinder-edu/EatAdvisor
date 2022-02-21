from django.urls import path

from . import views

# Creating URLConf
#api/v1/restaurants GET | POST
#api/v1/restaurants/1 GET | PUT | PATCH | DELETE

#api/v1/restaurants/1/reviews GET | POST
#api/v1/restaurants/1/reviews/11 GET | PUT | PATCH | DELETE

#api/v1/userprofile/current

#api/v1/reviews GET | POST


urlpatterns = [
    path("restaurants/", views.restaurants_list),
    path("restaurants/<int:pk>", views.restaurant_details),
    path("reviews/", views.reviews),
]