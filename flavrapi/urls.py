from django.urls import path 
from .views import RecipeListCreateAPIView, RecipeRetrieveUpdateDestroyAPIView

urlpatterns = [
        path('recipe/', RecipeListCreateAPIView.as_view(), name="recipe-list-create"),
        path('recipes/<uuid:id>/', RecipeRetrieveUpdateDestroyAPIView.as_view(), name="retrieve-update-delete")
]
