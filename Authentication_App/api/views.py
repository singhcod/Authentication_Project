
from  Authentication_App.models import Employee
from Authentication_App.api.serializers import EmployeeSerializer
from rest_framework import viewsets

# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

class Employee_ModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)

