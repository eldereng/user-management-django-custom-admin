from people.models import Person
from people.serializer import PersonSerializer
from rest_framework import viewsets

from django.contrib.auth.models import User
from people.serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]


class SignUpView(APIView):
    def post(self, request):
        user = User()
        user.password = request.data['password']
        user.username = request.data['username']
        user.save()
        user.set_password(user.password)
        user.save()
        token = Token.objects.get(user_id=user.id)
        user_serializer = UserSerializer(user)
        data = user_serializer.data
        data['token'] = token.key
        return Response(data, status=status.HTTP_201_CREATED)
