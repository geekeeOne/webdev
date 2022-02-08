from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	# return HttpResponse("Second Project")
	return render(request, 'dev_app/index.html')



def help(request):
	helpdict = {'help_insert':'HELP PAGE'}
	return render(request,'dev_app/help.html',context=helpdict)
# Create your views here.


def social(request):
	return render(request,'dev_app/social_example.html')


def blog(request):
	return render(request, 'dev_app/blog_example.html')


def portfolio(request):
	return render(request,'dev_app/portfolio.html')


def store(request):
	return render(request, 'dev_app/store_example.html')