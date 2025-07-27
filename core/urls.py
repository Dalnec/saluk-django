from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import ( SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView, )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url=reverse_lazy("admin:index"))),
    # swagger
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path( "api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui", ),
    path( "api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc", ),
    # apps
    path("api/", include("apps.person.routers"), name="person"),
    path("api/", include("apps.medicalhistory.routers"), name="medicalhistory"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = "rest_framework.exceptions.bad_request"

handler500 = "rest_framework.exceptions.server_error"