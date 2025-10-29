# backend/ainote_project/urls.py (ファイル全体をこれで上書きしてください)

from django.contrib import admin
from django.urls import path
# 👇 get_csrf_token と api_signup をインポート
from accounts.views import APILoginView, api_logout, api_root, api_signup, get_csrf_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='root'), 
    
    path('api/login/', APILoginView.as_view(), name='api_login'), 
    path('api/logout/', api_logout, name='api_logout'),           
    
    path('api/signup/', api_signup, name='api_signup'), 
    path('api/csrf/', get_csrf_token, name='api-csrf'),
]