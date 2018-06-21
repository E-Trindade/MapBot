from django.conf.urls import url
from django.conf.urls import include
from .views import mapbotFacebookView, mapbotAPIView

urlpatterns = [url(r'^mapbotwebhook/', mapbotFacebookView.as_view())]
urlpatterns = [url(r'^api/', mapbotAPIView.as_view())]
