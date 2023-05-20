from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, UserSignupSerializer, FollowSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# id 중복검사를 위한 모듈 import

# from .serializers import UsernameUniqueCheckSerializer


from django.contrib.auth import get_user_model
User = get_user_model()

# 회원 가입
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    print(1)
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')
    password_confirm = request.data.get('passwordConfirm')
    nickname = request.data.get('nickname')
    email = request.data.get('email')

    res_data = {}

    if User.objects.filter(username=username).exists():
        res_data['error'] = '중복된 ID입니다'
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(nickname=nickname).exists():
        res_data['error'] = '이미 존재하는 닉네임입니다.'
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(email=email).exists():
        res_data['error'] = '이미 가입한 이력이 있는 이메일입니다.'
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
    
    if password != password_confirm:
        res_data['error'] = '비밀번호가 다릅니다.'
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSignupSerializer(data=request.data)
    print(2)
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


@api_view(['GET'])
def userContent(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    print(user)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    # 장고에 내장되어 user class를 만들어서 기능을 구현을 위해 사용
    res_data = {} 
    person = get_object_or_404(get_user_model(), username=username)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    else:
        res_data['err'] = '본인은 팔로우 불가능합니다.'
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
    serializer = FollowSerializer(person)
    # follow_status = {
    #         'follow' : follow,
    #         # 팔로워 숫자
    #         'count' : person.followings.count(), 
    #         # 팔로워 목록
    #         'follow_list' : serializer.data.get('followings'),
    #         # 팔로잉 수
    #         'following_count' : person.followers.count(),
    #     }
    # return JsonResponse(follow_status)
    return Response(serializer.data)