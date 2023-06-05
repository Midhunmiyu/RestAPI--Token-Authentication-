from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


'''Browsable api is not suitable for token authentication, so httpie is used in this project to do operations

http DELETE http://127.0.0.1:8000/studentapi/ for read(GET)
http DELETE http://127.0.0.1:8000/studentapi/4/ 'authorization:token 81ecaa774b87928e55d72020fd616cc767bcbb39' for DELETE
http PUT http://127.0.0.1:8000/studentapi/4/ name=jay roll=106 city=kannur 'authorization:token 81ecaa774b87928e55d72020fd616cc767bcbb39' for UPDATE
http -f POST http://127.0.0.1:8000/studentapi/ name=jay roll=106 city=kannur 'authorization:token 81ecaa774b87928e55d72020fd616cc767bcbb39' for POST

were the studentapi in the link is from router.register('studentapi', views.StudentModelViewSet, basename='student')'''
