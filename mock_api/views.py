"""Module for handing json data."""
import json
from django_ratelimit.decorators import ratelimit
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from mock_api.models import API
from mock_api.decorators import cache_response

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class Home(generic.ListView):
    """Main landing page of project"""
    template_name = 'home.html'
    model = API


@ratelimit(key='ip', rate='10/m', block=True)
def add_project(request):
    """Function for adding JSON response of GET and/or POST methods for provided project and resource name"""
    validation_result = ""
    if request.method == 'POST':
        fetched_project_name = request.POST['project_name']
        fetched_resource_name = request.POST['resource_name']
        fetched_json_response = request.POST['json_response']
        fetched_method = request.POST['method']
        # JSON validation
        try:
            fetched_json_response = json.loads(
                fetched_json_response) if fetched_json_response else None
            API.objects.update_or_create(
                project_name=fetched_project_name,
                resource_name=fetched_resource_name,
                method=fetched_method,
                defaults={
                    'json_response': fetched_json_response
                }
            )
            cache_key = (fetched_method, fetched_project_name,
                         fetched_resource_name)
            if cache_key in cache:
                cache.delete(cache_key)
            validation_result = "Form Submitted Successfully"
        except Exception:
            validation_result = "ERROR: Invalid JSON"

    my_context = {
        'submission_result': validation_result
    }
    return render(request, 'add_project.html', my_context)


@ratelimit(key='ip', rate='10/m', block=True)
@cache_response
def get_json_response(request, project_name, resource_name):
    """Function for getting the JSON response for mentioned project, resource name and method"""
    try:
        api_obj = API.objects.get(
            project_name=project_name, resource_name=resource_name, method=request.method)
        return JsonResponse(api_obj.json_response, safe=False, json_dumps_params={'indent': 4})
    except Exception:
        error_msg = f"Error fetching record: project : {
            project_name}, resource : {resource_name}, method : {request.method}"
        return JsonResponse(error_msg, status=404, safe=False, json_dumps_params={'indent': 4})
