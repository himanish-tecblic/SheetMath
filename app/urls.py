from django.urls import path
from rest_framework.routers import DefaultRouter
from app.views import PBPMApi
router = DefaultRouter()
router.register("pbpm", PBPMApi, basename="Item Status API")

urlpatterns = [

]+ router.urls