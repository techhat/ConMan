# Create your views here.
from django.shortcuts import render_to_response
from common.models import *

def testtemplate(request):
    
    return render_to_response('test_template.html',None)

