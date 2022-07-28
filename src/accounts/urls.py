from django.urls import include, path
from accounts.views import login_user, register_user

app_name = "accounts"

urlpatterns = [
    path("account/", login_user, name="login"),
    path("register/", register_user, name="register"),

]