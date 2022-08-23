from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Company Card
    path('card/',                  views.UsersCardListView.as_view(),           name='companyCard'),
    path('card/<int:id>/',         views.UsersCardRetrieveView.as_view(),       name='companyCardShow'),
    path('card/create/',           views.UserCardCreateView.as_view(),          name='companyCardSCreate'),
    path('user/',                  views.UsersListView.as_view(),               name="userList"),
    path('card/list/',             views.CardUserListView.as_view(),            name="ListCard"),
    path('business/card/',         views.BusinessCardListView.as_view(),        name="BusinessCard"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
 