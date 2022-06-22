from asyncio import TimerHandle
import imp
from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta
from django.utils import timezone

# datetime field와 비교 시
# (datetime)user.join_date > datetime.now() ->에러
# (datetime)user.join_date > timezone.now() ->정상

class RegistedMoretThanAWeekUser(BasePermission):
    
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        return bool(request.user.join_date < (datetime.now().date() - timedelta(days=-1)))


class RegistedMoretThanThreeUser(BasePermission):
    
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        return bool(request.user.join_date < (timezone.now() - timedelta(minutes=1)))
