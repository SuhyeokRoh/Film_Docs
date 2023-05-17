from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    # Id, pw, pw확인 request.data를 통해 전달

    password = request.data.get('password')
    password_confirm = request.data.get('passwordConfirm')
    if password != password_confirm:
        return Response({'error':'비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    # print(serializer)
    # 유효성 검사
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 비밀번호 hash해서 저장
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)