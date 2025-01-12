from django.urls import path


from rooms import views as room_view

app_name = "rooms"
urlpatterns = [

    path("room/<int:pk>/detial/", room_view.room_details, name="room_detail"),

]