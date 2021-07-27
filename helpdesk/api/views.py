from api.serializers import HelpdeskSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser

from search.documents import HelpdeskDocument


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['username'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'That username has already been taken. Please choose a new username'},
                                status=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error': 'Could not login. Please check username and password'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=200)


class SeearchList(generics.ListAPIView):
    serializer_class = HelpdeskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        query = self.request.query_params.get('query')
        s = HelpdeskDocument.search().query("match", title=query).query("match", details=query)
        qs = s.to_queryset()
        return qs
