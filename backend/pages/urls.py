"""guide_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guides', views.guides, name='guides'),
    path('submitted', views.submitted, name='submitted'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('project-details', views.project_details, name='project-details'),
    path('select-guide', views.select_guide, name='select-guide'),
]
