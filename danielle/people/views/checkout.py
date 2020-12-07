from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from people.serializers import CheckoutSerializer


class CheckoutCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CheckoutSerializer