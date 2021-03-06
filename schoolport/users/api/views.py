from re import U, search
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from schoolport.users.models import User
from schoolport.users.api.serializers import RegistrationSerializer, UserInfoSerializer


@api_view(['POST', ])
@authentication_classes([])
@permission_classes([])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['result'] = True
            data['response'] = "successfully registerd a new user."
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
            data['result'] = False
        
        return Response(data)
        

@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def userinfo_view(request):
    #print(request.user)
    #username = request.data['userid']
    try:
        user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)
