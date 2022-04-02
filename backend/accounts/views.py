from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
User = get_user_model()


class SignUpView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        # if email == '':
        #     return Response({'error': 'Email field can not be empty'}, status=status.HTTP_400_BAD_REQUEST)

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                if len(password) < 6:
                    return Response({'error': 'Password must be at least 6 characters in length'}, status=status.HTTP_400_BAD_REQUEST)
                elif email == '':
                    return Response({'error': 'Email field can not be empty'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    user = User.objects.create_user(
                        email=email, password=password, name=name)
                    user.save()
                    return Response({'success': f'User-({name}) created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
