"""
URL configuration for ainote_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from accounts.views import APILoginView, api_logout, api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    # 👇 APIエンドポイントを設定
    path('api/login/', APILoginView.as_view(), name='api_login'), 
    path('api/logout/', api_logout, name='api_logout'), 
    
    path('', api_root, name='root'), # http://localhost:8000/ に対応
    # path('accounts/', include('django.contrib.auth.urls')), # テンプレートベースの認証URLは削除またはコメントアウト
]