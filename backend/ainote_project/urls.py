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
from accounts.views import get_csrf_token
from accounts.views import APILoginView, api_logout, api_root, api_signup

urlpatterns = [
    path('admin/', admin.site.urls),
    # ⚠️ 1. ルートパスを追加
    path('', api_root, name='root'), 
    
    # 2. 既存のログイン/ログアウト
    path('api/login/', APILoginView.as_view(), name='api_login'), 
    path('api/logout/', api_logout, name='api_logout'),           
    
    # ⚠️ 3. サインアップAPIを追加
    path('api/signup/', api_signup, name='api_signup'), 
    
    #CSRF用のトークン
    path('api/csrf/', get_csrf_token, name='api-csrf'),

]