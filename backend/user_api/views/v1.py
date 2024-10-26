from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework_simplejwt.tokens import RefreshToken

from user_api.models import User

from user_api.serializers.v1 import UserSerializer


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
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


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        credential = request.data.get('credential', None)
        password = request.data.get('password', None)

        if not credential:
            return Response({
                'errors': ['Log in credential missing.'],
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=credential)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=credential)
            except User.DoesNotExist:
                user = None

        if user is None:
            return Response({
                'errors': ['User not found.'],
            }, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({
                'errors': ['Invalid password'],
            }, status=status.HTTP_401_UNAUTHORIZED)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Successfully log in!',
            })
        else:
            return Response({
                'detail': 'Invalid credentials.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve user's profile",
        responses={
            200: openapi.Response(
                description="User profile data", schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(
                            type=openapi.TYPE_INTEGER, description="User ID"
                        ),
                        "username": openapi.Schema(
                            type=openapi.TYPE_STRING, description="Username"
                        ),
                        "email": openapi.Schema(
                            type=openapi.TYPE_STRING, description="Email"
                        ),
                    }
                )
            ),
            401: openapi.Response(description="User is not authenticated"),
            404: openapi.Response(description="User not found"),
        },
    )
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk:
            try:
                user = User.objects.get(pk=pk)
            except User.DoesNotExist:
                return Response({
                    'details': 'User not found',
                }, status=status.HTTP_404_NOT_FOUND)

            if user.is_private and request.user.is_anonymous:
                return Response({
                    'details': 'User is not authenticated',
                }, status=status.HTTP_401_UNAUTHORIZED)

            serializer = UserSerializer(user)

            return Response(serializer.data)

        user = request.user

        if user.is_anonymous:
            return Response({
                'details': 'User is not authenticated',
            }, status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserSerializer(user)
        data = serializer.data

        return Response(data)
