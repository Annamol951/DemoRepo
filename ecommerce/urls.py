"""ecommerce URL Configuration

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
# from django.contrib import admin
# # from django.urls import path
# from django.urls import path,include
# from ecomapp.views import home

# from ecomapp.views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('h/',home),
#      path('accounts/',include('django.contrib.auth.urls')),

# ]
"""OnlineShopping URL Configuration
 
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
# from ecomapp.views import addProduct, home, loginPage, logoutPage, placeOrder, registerPage
from ecomapp.views import *
from django.contrib import admin  
from django.urls import path, include  
from django.conf import settings
from django.conf.urls.static import static


 
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', home ,name='home'),
    path('Api/basic/', CustomerView.as_view()), 
    path('Api/order/', OrderView.as_view()),
    path('placeOrder/<str:i>/', placeOrder,name='placeOrder'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),
    path('addProduct/', addProduct,name='addProduct'),
    
    ]
    


    
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



#  username : emom02
#  email : emo02@gmail.com
# password : emom@123
# url(customer api) : http://127.0.0.1:8000/Api/basic/
#  url(order api)http://127.0.0.1:8000/Api/order/