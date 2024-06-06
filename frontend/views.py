# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render

def index(request):
  # context is how you would pass data into the template
  return render(request, 'index.html')
  # template = loader.get_template('index.html')

  # return HttpResponse(template.render({}, request))

def about(request):
  return render(request, 'about.html')
