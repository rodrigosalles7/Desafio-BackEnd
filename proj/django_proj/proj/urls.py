from django.urls import path
from proj import views

urlpatterns = [
    path("", views.ListProjAPIView.as_view(), name="proj_list"),
    path("create/", views.CreateProjAPIView.as_view(), name="proj_create"),
    path("update/<str:pk>/", views.UpdateProjAPIView.as_view(), name="update_proj"),
    path("delete/<str:pk>/", views.DeleteProjAPIView.as_view(), name="delete_proj"),
]
