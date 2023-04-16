from django.shortcuts import render
from django.http import JsonResponse
from .oai_queries import get_completion


def query_view(request):
    prompt = request.GET.get('prompt')
    user = request.GET.get('user')
    response = get_completion(prompt, user=user)
    return JsonResponse({'response': response})
