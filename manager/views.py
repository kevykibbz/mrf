from manager.decorators import unauthenticated_user,allowed_users
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Oders,ExtendedAuthUser,OrderFields,UserFileUploads
from django.contrib.auth.models import User,Group,Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse,HttpResponse
from installation.models import SiteConstants
from django.shortcuts import redirect
#from .forms import *
from django.core.paginator import Paginator
from django.contrib.sites.shortcuts import get_current_site
from .addons import send_email,getSiteData
import json
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from django.contrib.auth import update_session_auth_hash
import re
from .search import *
import datetime
from django.contrib.humanize.templatetags.humanize import intcomma
from django.template.defaulttags import register


def dashboard(request):
    obj=SiteConstants.objects.count()
    if obj == 0:
        return redirect('/installation')
    else:
        obj=SiteConstants.objects.all()[0]
        data={
                'title':'Welcome',
                'obj':obj,
                'data':request.user,
            }
        return render(request,'manager/index.html',context=data)

def overview(request):
    obj=SiteConstants.objects.count()
    if obj == 0:
        return redirect('/installation')
    else:
        obj=SiteConstants.objects.all()[0]
        data={
                'title':'Overview',
                'obj':obj,
                'data':request.user,
            }
        return render(request,'manager/overview.html',context=data)

def queries(request,id):
    obj=SiteConstants.objects.count()
    if obj == 0:
        return redirect('/installation')
    else:
        obj=SiteConstants.objects.all()[0]
        data={
                'title':'Queries',
                'obj':obj,
                'data':request.user,
            }
        return render(request,'manager/queries.html',context=data)
