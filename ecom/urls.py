from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include("store.urls")),
    path('', include("home.urls")),
    path('cart/', include("cart.urls")),
    path('payment/', include("payment.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'T-Lab Administration'
