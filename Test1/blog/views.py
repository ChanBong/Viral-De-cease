from django.shortcuts import render
from django.http import HttpResponse
import sys
from subprocess import run, PIPE


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def covid(request):
    return render(request, 'blog/covid.html')


def aids(request):
    return render(request, 'blog/aids.html')


def rabies(request):
    return render(request, 'blog/rabies.html')


def diseas_library(request):
    return render(request, 'blog/diseas_library.html')


def commoncold(request):
    return render(request, 'blog/commoncold.html')


def h1n1(request):
    return render(request, 'blog/h1n1.html')


def hepatitisa(request):
    return render(request, 'blog/hepatitisa.html')


def hepatitisb(request):
    return render(request, 'blog/hepatitisb.html')
