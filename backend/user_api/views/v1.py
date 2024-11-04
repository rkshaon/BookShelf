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

    @swagger_auto_schema(
        operation_description="Register a new user.",
        request_body=UserSerializer,
        responses={
            201: openapi.Response(
                description="User registered successfully",
                examples={
                    "application/json": {
                        "message": "User registered successfully"
                    }
                }
            ),
            400: "Bad Request - Validation errors"
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                'message': 'User registered successfully',
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Log in a user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "credential": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="User email or username"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="User password"
                ),
            }
        ),
        responses={
            200: openapi.Response(
                description="User login data", schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "refresh": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Refresh token"
                        ),
                        "access": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Access token"
                        ),
                        "message": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Success message"
                        ),
                    }
                )
            ),
            400: openapi.Response(description="Log in credential missing"),
            401: openapi.Response(description="Invalid password"),
            404: openapi.Response(description="User not found"),
        },
    )
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

        if not user:
            return Response({
                'detail': 'Invalid credentials.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': 'Successfully log in!',
        })


class UserProfileView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve user's profile",
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="Bearer <JWT Token>",
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ],
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


class RefreshTokenView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Refresh access token",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "refresh": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Refresh token"
                ),
            }
        ),
        responses={
            200: openapi.Response(
                description="New access token", schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "access": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Access token"
                        ),
                        "message": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Success message"
                        ),
                    }
                )
            ),
            400: openapi.Response(description="Refresh token missing"),
            401: openapi.Response(description="Invalid refresh token"),
        },
    )
    def post(self, request, *args, **kwargs):
        refresh = request.data.get('refresh', None)

        if not refresh:
            return Response({
                'errors': ['Refresh token missing.'],
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh)
            # token.blacklist()
            # new_token = RefreshToken.for_user(token.user)
            new_access_token = token.access_token
        except Exception:
            return Response({
                'errors': ['Invalid refresh token.'],
            }, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            'access': str(new_access_token),
            'message': 'Successfully refreshed access token!',
        })
