from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user_api.serializers.v1 import UserSerializer


class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(f"Serializer Data: {serializer.data}")

            return Response({
                'message': 'User registered successfully',
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
