from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
import subprocess

def index(request):
  # context is how you would pass data into the template
  return render(request, 'index.html')
  # template = loader.get_template('index.html')

  # return HttpResponse(template.render({}, request))

def about(request):
  return render(request, 'about.html')

def collect_speed_info(request):
  if request.method == 'POST':
    try:
      subprocess.run(['python3', 'collect_speed_info.py'])
      
      # return HttpResponse('Script Executed!')
      return render(request, 'results.html')
    except subprocess.CalledProcessError as e:
      return HttpResponse(f'Script Execution error: {e.stderr}')
    