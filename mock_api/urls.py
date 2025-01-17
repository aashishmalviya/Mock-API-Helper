from django.urls import path
from .views import Home, add_project, get_json_response

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-project/', add_project, name='add-project'),
    path('<str:project_name>/<str:resource_name>/', get_json_response),
]
