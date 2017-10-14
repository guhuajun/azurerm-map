# -*- encoding: utf-8 -*-

from rest_framework import routers

from backend import views

router = routers.DefaultRouter(trailing_slash=False)

router.register('cmdlet', views.CmdletViewSet)
router.register('cmdletparameter', views.CmdletParameterViewSet)
router.register('cmdletoutputtype', views.CmdletOutputTypeViewSet)

urlpatterns = router.urls
