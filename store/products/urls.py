from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('products', views.products, name="products"),
    path('<int:category_id>/', views.products, name="products"),
    path('basket-add/<int:product_id>', views.basket_add, name='basket_add'),
    path('basket-delete/<int:id>', views.basket_delete, name='basket_delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
