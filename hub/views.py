from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.backends import *
from django.conf import settings


# Create your views here.


def homepage(request):
    return render(request, 'hub/homepage.html', {

})



def our_organization(request):
    return render(request, 'hub/our_organization.html', {

})



def why_orphan_education(request):
    return render(request, 'hub/why_orphan_education.html', {

})

def get_involved(request):
    return render(request, 'hub/get_involved.html', {

})

def our_impact(request):
    return render(request, 'hub/our_impact.html', {

})


def sign_in(request):
    return render(request, 'hub/sign_in.html', {

})




def sign_out(request):
    return render(request, 'hub/sign_out.html', {

})






