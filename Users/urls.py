from django.urls import path

from Users.views import UpdateUserAPIView, DestroyUserAPIView, CreateUserAPIView

app_name = 'Users'

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('update/<int:user_id>/', UpdateUserAPIView.as_view()),
    path('delete/<int:user_id>/', DestroyUserAPIView.as_view()),
]
