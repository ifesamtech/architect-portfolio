from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    # path('upload/', views.upload_cv, name='upload'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('project/<str:pk>/', views.project_details, name='project-details'),
    path('add-projects/', views.add_projects, name='add-projects'),
    path('add-category/', views.add_category, name='add-category'),
    path('edit-project/<str:pk>/', views.edit_project, name='edit-project'),
    path('delete/project/<str:pk>', views.delete_project, name='delete-project'),
    ]