from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
        path('', TemplateView.as_view(template_name='index.html')),

]
