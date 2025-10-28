# backend/accounts/views.py

from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.contrib.auth import logout # ログアウトに必要

def api_root(request):
    """ルートパスがアクセスされたときに実行される"""
    return JsonResponse({'status': 'ok', 'message': 'Django backend is running correctly. Access /api/login/ for authentication.'})

@method_decorator(csrf_exempt, name='dispatch') # 開発環境でブラウザ/ReactからのPOSTを許可
class APILoginView(LoginView):
    def post(self, request, *args, **kwargs):
        # ... (前回の回答で示した認証ロジック) ...
        super().post(request, *args, **kwargs)
        
        if request.user.is_authenticated:
            return JsonResponse({'success': True, 'username': request.user.username})
        else:
            return JsonResponse({'success': False, 'message': '認証情報が不正です'}, status=401)

@csrf_exempt
def api_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'POSTメソッドが必要です'}, status=405)