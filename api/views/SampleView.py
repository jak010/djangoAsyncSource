from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from .. import tasks


class TestView(APIView):

    def get(self, request):
        print(tasks.add.delay(1, 1).get())

        return Response(data={'a': 'b'}, content_type='application/json')
