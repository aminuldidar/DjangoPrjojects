from django.shortcuts import render

def hello(request):
	print("Here it is")
	return render(request,"hello.html",{})
