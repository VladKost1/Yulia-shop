from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import (CategoryViewSet, ProductDeleteView, ProductDetailView,
                       ProductListView, ProductUpdateView, UserViewSet)

app_name = "api"

router = routers.DefaultRouter()
router.register("customers", UserViewSet)

router1 = routers.SimpleRouter()
router1.register(r"category", CategoryViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Shop API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(router1.urls)),
    path("auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
    path("product/", ProductListView.as_view(), name="product_list"),
    path("<uuid:uuid>/", ProductDetailView.as_view(), name="product_details"),
    path("product/<uuid:uuid>/", ProductUpdateView.as_view(), name="product_update"),
    path("product/delete/<uuid:uuid>/", ProductDeleteView.as_view(), name="product_update"),

]
