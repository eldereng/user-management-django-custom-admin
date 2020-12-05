from rest_framework.response import Response
# from rest_framework import status

from people.models import Person
from people.models import Checkin
from people.serializers import PersonSerializer
from people.serializers import UserSerializer
from people.serializers.checkin import CheckinSerializer

from rest_framework import viewsets
from rest_framework import generics
# from rest_framework.views import APIView

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth import authenticate


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]


"""
class CheckinViewSet(viewsets.ModelViewSet):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    permission_classes = [IsAuthenticated]
"""


class CheckinCreateView(generics.CreateAPIView):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    permission_classes = [IsAuthenticated]


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class UserRetrieve(generics.RetrieveAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer


"""
class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(
        self,
        request,
    ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"},
                            status=status.HTTP_400_BAD_REQUEST)
"""


class CustomObtainAuthToken(ObtainAuthToken):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken,
                         self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'id': token.user_id,
        })
