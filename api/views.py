from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .Num2Words import Num2Words
import json


def handler_not_found(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found'
    })


def handler_server_error(request):
    return JsonResponse({"status": 500,
                         "error": "Unfortunately we're having trouble loading the page you are looking for."})


@csrf_exempt
def num_to_english(request):
    try:
        if request.method not in ("POST", "GET"):
            return JsonResponse({"status": 'error',
                                 "num_in_english": f'{request.method} is not allowed'
                                 })
        data = json.loads(request.body) if request.method == "POST" else request.GET
        number = data.get('number')

        if number and number.isnumeric():
            # convert a number to the english words
            words = Num2Words.convert(int(number))
        else:
            words = 'Error: Invalid input.'

        code = "error" if 'Error' in words else "ok"
        return JsonResponse({"status": code,
                             "num_in_english": words
                             })
    except json.decoder.JSONDecodeError:
        return JsonResponse({"status": 'error',
                             "num_in_english": 'Incorrect JSON format'
                             })
    except Exception as e:
        return JsonResponse({"status": 'error',
                             "num_in_english": f'Internal error {e}'
                             })


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Convert a number to the words (Django)': '/num_to_english',
        'Convert a number to the words(Django Rest Framework)': '/num_to_english1',
    }
    return Response(api_urls)


@api_view(['GET', 'POST'])
def num_to_words(request):
    try:
        data = request.data if request.method == "POST" else request.query_params
        number = data.get('number')

        if number and number.isnumeric():
            # convert a number to the english words
            words = Num2Words.convert(int(number))
        else:
            words = 'Error: Invalid input.'

        code = "error" if 'Error' in words else "ok"
        return Response({"status": code,
                         "num_in_english": words
                         })
    except Exception as e:
        return Response({"status": 'error',
                         "num_in_english": f'Internal error {e}'
                         })
