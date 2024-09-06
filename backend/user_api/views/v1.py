from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user_api.serializers.v1 import UserSerializer


class UserRegistrationView(APIView):
    """
    post:
    Register a new user.

    Takes in user details and creates a new user in the system.

    Parameters:
        None

    Returns:
        message: A success message if the registration is successful.
        errors: If the validation fails, returns a list of errors with
            their descriptions.
    """
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(f"Serializer Data: {serializer.data}")

            return Response({
                'message': 'User registered successfully',
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
