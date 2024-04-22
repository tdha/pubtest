import json
from django.http import JsonResponse, QueryDict


class JsonMiddleware:
    invalid_json_http_status = 400
    invalid_json_response = {'error': 'Invalid JSON request'}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method in ('GET', 'POST') \
                and (content_type := request.META.get('CONTENT_TYPE')) \
                and 'application/json' in content_type.lower():
            try:
                data = json.loads(request.body)
            except ValueError:
                return JsonResponse(
                    self.invalid_json_response,
                    status=self.invalid_json_http_status)

            if isinstance(data, dict):
                querydict = QueryDict(mutable=True)
                querydict.update(data)
                # set either request.GET or request.POST
                setattr(request, request.method, querydict)
        
        return self.get_response(request)
