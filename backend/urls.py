# stock_portal/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api/accounts/", include("accounts.urls")),  # ✅ keep this one
]
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"status": "ok", "message": "Backend Running Successfully!"})

urlpatterns = [
    path("", home),  # 👈 add this line
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api/accounts/", include("accounts.urls")),
]
