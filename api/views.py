from django.shortcuts import render, render_to_response
from django.template import RequestContext
from rest_framework import request
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import json


@api_view(http_method_names=['GET'])
@permission_classes((permissions.AllowAny,))
def getUserList(request):
    return Response([
        {"name": "admin", "password": "123"},
        {"name": "auditor", "password": "456"},
    ])


@api_view(http_method_names=['POST'])
@permission_classes((permissions.AllowAny,))
def setUser(request):
    return Response({
        "data": request.data,
        "test": "111"
    })