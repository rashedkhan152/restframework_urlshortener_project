from rest_framework.decorators import api_view
from rest_framework.response import Response
from knox.auth import AuthToken


from django.views import View




@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info':{
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                },
        })

    return Response({'error': 'not authenticated'}, status=400)