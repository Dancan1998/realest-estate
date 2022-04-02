from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status


class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        try:
            send_mail(
                data['subject'],
                'Name: '
                + data['name']
                + '\nEmail: '
                + data['email']
                + '\n\nMessage:\n'
                + data['message'],
                'dancankingstar@gmail.com',  # YOUR SENDER EMAIL FROM YOUR SETTINGS
                # EMAIL YOU ARE SENDING TO
                ['dancankingstar@gmail.com', 'dancanchibole8.gmail.com'],
                fail_silently=True
            )

            contact = Contact(name=data['name'], email=data['email'],
                              subject=data['subject'], message=data['message'])
            contact.save()

            return Response({'success': 'Message sent successfully'}, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Message failed to send'}, status=status.HTTP_400_BAD_REQUEST)
