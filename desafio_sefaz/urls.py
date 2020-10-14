from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.base.views import Home
from app.processamento.views import ClassificacaoViewSet

router = routers.DefaultRouter()
router.register(r'processamento', ClassificacaoViewSet )

urlpatterns = [
    path('', Home.as_view()),
    path('regra/', include('app.processamento.urls', namespace='processamento')),
    path('produto/', include('app.base.urls', namespace='base')),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
