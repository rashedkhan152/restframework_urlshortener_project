from rest_framework.decorators import api_view
from rest_framework.response import Response
from knox.views import LoginView as KnoxLoginView

from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from users.selializers import LoginSerializer


from django.views import View


#User login
@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token = AuthToken.objects.create(user)

    return Response({
        'user_info':{
            'id': user.id,
            'username': user.username,
            'password': user.password
            },
        'token': token    
    })

