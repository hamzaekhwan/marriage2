from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('invite_request', views.invite_request, name='invite_request'),
    path('my_invites', views.my_invites, name='my_invites'),
    path('make_invite', views.make_invite, name="make_invite"),
    path('login', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)