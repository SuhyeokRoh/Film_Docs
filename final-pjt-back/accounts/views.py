from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

# id 중복검사를 위한 모듈 import

# from .serializers import UsernameUniqueCheckSerializer



from django.contrib.auth import get_user_model
User = get_user_model()

# 회원 가입
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    # print(request)
    username = request.data.get('username')
    password = request.data.get('password')
    password_confirm = request.data.get('passwordConfirm')
    nick_name = request.data.get('nick_name')
    email = request.data.get('email')
    res_data = {}

    if User.objects.filter(username=username).exists():
        res_data['error'] = '중복된 ID입니다'
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
    

    if password != password_confirm:
        res_data['error'] = '비밀번호가 다릅니다.'
        # print(res_data)
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    # print(serializer)
    # 유효성 검사
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 비밀번호 hash해서 저장
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 회원 탈퇴
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def account_delete(request):
    request.user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)