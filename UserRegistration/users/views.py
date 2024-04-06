from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny



@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_registration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully.', 'user_id': serializer.data['id']})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_details(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def referrals(request):
    user = request.user
    referrals = User.objects.filter(referral_code=user.referral_code)
    serializer = UserSerializer(referrals, many=True)
    return Response(serializer.data)
