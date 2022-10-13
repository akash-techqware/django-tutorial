from encodings import utf_8
from django.shortcuts import render
from django.http import HttpResponse
from  . models import Job
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def index(request):
    return HttpResponse("hello world")
@csrf_exempt
def job(request):
    if request.method == "GET":
        jobs=Job.objects.all()
        # API Use
        # result = []

        # jobs=Job.objects.all()
        # for job in jobs:
        #     data={
        #         "company": job.company,
        #         "description": job.description
        #     }
        #     result.append(data)

        # return HttpResponse(json.dumps(result))
        return render(request, 'portfolio/index.html', {"jobs": jobs})
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        company= data['company']
        description= data['description']
        job= Job(company=company, description=description)
        job.save()
        # API Use
        return HttpResponse({"Company added Successfully !"})


    if request.method == "DELETE":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        company= data['company']

        job =Job.objects.filter(company=company).delete()
        # API Use
        return HttpResponse({"Company delete Successfully !"})
