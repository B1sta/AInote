# backend/accounts/views.py (修正後の全文)

from django.contrib.auth.views import LoginView
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt # 削除
from django.utils.decorators import method_decorator
import json
from django.contrib.auth import logout
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie # インポート

@ensure_csrf_cookie 
def get_csrf_token(request):
    """CSRFトークンをクッキーにセットして返す"""
    return JsonResponse({'detail': 'CSRF cookie set'})

# @csrf_exempt を削除
def api_root(request):
    """ルートパスがアクセスされたときに実行される"""
    return JsonResponse({'status': 'ok', 'message': 'Django backend is running correctly. Access /api/login/ for authentication.'})

# @method_decorator(csrf_exempt...) を削除
class APILoginView(LoginView):
     def post(self, request, *args, **kwargs):
         super().post(request, *args, **kwargs)
        
         if request.user.is_authenticated:
             return JsonResponse({'success': True, 'username': request.user.username})
         else:
             return JsonResponse({'success': False, 'message': '認証情報が不正です'}, status=401)

# @csrf_exempt を削除
def api_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'POSTメソッドが必要です'}, status=405)

# @csrf_exempt を削除
def api_signup(request):
    """新しいユーザーアカウントを作成するAPI"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email', '') 

            if not username or not password:
                return JsonResponse({'success': False, 'message': 'ユーザー名とパスワードは必須です'}, status=400)

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return JsonResponse({'success': True, 'message': 'アカウントが正常に作成されました'}, status=201)

        except IntegrityError:
            return JsonResponse({'success': False, 'message': 'このユーザー名は既に使用されています'}, status=409)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': '無効なJSONデータです'}, status=400)
        except Exception as e:
            print(f"Signup error: {e}")
            return JsonResponse({'success': False, 'message': 'サーバー側でエラーが発生しました'}, status=500)

    return JsonResponse({'error': 'POSTメソッドが必要です'}, status=405)