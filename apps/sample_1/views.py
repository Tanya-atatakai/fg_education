from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .runner import Runner


@csrf_exempt
def json_to_html(request):
    json_input = request.body.decode('utf-8')
    return HttpResponse(Runner.convert_json2html(json_input))
