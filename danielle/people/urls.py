from django.urls import path, include
from people import views

# ViewSet class based views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('people', views.PersonViewSet)

urlpatterns = [path('', include(router.urls))]
