from django.conf.urls import url, include
from rest_framework import routers

from . import views as views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'bracket', views.BracketViewSet)
router.register(r'competitor', views.CompetitorViewSet)
router.register(r'position', views.PositionViewSet)


urlpatterns = [
    url(r'^$', views.bracket_view, name='bracket_view'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^hello/', views.hello_world)
]
