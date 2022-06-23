from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView #  permission_classes를 이용하기 위해 임포트해서 씀 
from rest_framework import permissions
from django.contrib.auth import login, logout, authenticate
from django.db.models import F
from user.models import UserProfile
from user.serializers import UserSerializer

from ai.permissions import RegistedMoretThanThreeUser
from ai.permissions import IsAdminOrIsAuthenticatedReadOnly

# Create your views here.

class UserView(APIView): # CBV 방식
    # permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]
    # 사용자 정보조회
    def get(self, request):
        return Response(UserSerializer(request.user).data)
        # hobbys = user.userprofile.hobby.all()
        # for hobby in hobbys:
        # exclde : 매칭 된 쿼리만 제외, filter와 반대
        # annotate : 필드 이름을 변경해주기 위해 사용, 이외에도 원하는 필드를 추가하는 등 다양하게 활용 가능
        # values / values_list : 지정한 필드만 리턴 할 수 있음. values는 dict로 return, values_list는 tuple로 ruturn
        # F() : 객체에 해당되는 쿼리를 생성함
            # hobby_members = hobby.userprofile_set.exclude(user=user).annotate(username=F('user__username')).values_list('username', flat=True)
            # hobby_members = list(hobby_members)
            # print(f"hobby : {hobby.name} / hobby members : {hobby_members}")

        
        
     # 회원가입
    def post(self, request):
        user = request.user
        return Response({'message': 'post method!!'})

     # 회원 정보 수정
    def put(self, request):
        return Response({'message': 'put method!!'})
    
     # 회원 탈퇴
    def delete(self, request):
        return Response({'message': 'delete method!!'})

class UserAPIView(APIView): # CBV 방식
    permission_classes = [permissions.AllowAny]

    # 로그인 
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)

        if not user: 
            return Response({"error":"존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})
        
        else:
            login(request, user)

        return Response({"message":"login success!!"})

    def delete(self, request):
        logout(request)
        return Response({"message":"logout success!!"})




