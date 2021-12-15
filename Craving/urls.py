"""Craving URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import urls
from user_role import urls as RoleUrls
from user_profile import urls as ProfileUrls
from ingredient import urls as IngredientUrl
from recipe import urls as RecipeUrls
from order import urls as OrderUrls
from recipe_ingredient import urls as recipe_ingredient_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
    path('',include(RoleUrls)),
    path('',include(ProfileUrls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # new
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',include(IngredientUrl)),
    path('',include(RecipeUrls)),
    path('',include(OrderUrls)),
    path('',include(recipe_ingredient_urls)),
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
