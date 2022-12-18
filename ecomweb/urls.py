"""ecomweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_here, name='login'),
    path('log-out/', views.log_out,name='logout'),
    path('blogs/', views.blogs, name='blogs'),
    path('full-blog/<slug>', views.fulllblog, name='fulllblog'),
    path('all-products/', views.allproducts, name='allproducts'),
    path('product-view/', views.prodview, name='productview'),
    path('add-to-cart/', views.add_to_cart, name='addcart'),
    path('cart/', views.cart_page, name='cart'),
    path('increase-quantity/', views.increase_quantity, name='increase-quantity'),
    path('decrease-quantity/', views.decrease_quantity, name='decrease-quantity'),
    path('remove-quantity/', views.remove_quantity, name='remove-from-cart'),
    path('about-us/', views.About_us, name='aboutus'),
    path('Privacy-Policy/', views.privacy_policy, name='privacypolicy'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
