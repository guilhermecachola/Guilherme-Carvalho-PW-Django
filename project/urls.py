from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from filmes.api import api as filmes_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", filmes_api.urls),
    path("escola/", include("escola.urls")),
    path("portfolio/", include("portfolio.urls")),
    path("accounts/", include("accounts.urls")),
    path("artigos/", include("artigos.urls")),
    path("", lambda request: redirect('portfolio_index')),
]