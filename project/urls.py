from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("escola/", include("escola.urls")),
    path("portfolio/", include("portfolio.urls")),
    path("accounts/", include("accounts.urls")),
    path("artigos/", include("artigos.urls")),
    path("", include("escola.urls")),
]