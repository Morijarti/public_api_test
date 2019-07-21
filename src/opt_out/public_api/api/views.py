from django.http import JsonResponse, HttpRequest, HttpResponse
from opt_out.public_api.api.models import Submission


def submit(request: HttpRequest) -> JsonResponse:
    item = Submission()

    item.url = request.POST["urls"]

    item.save()
    response = {"submission_id": item.submission_id}
    return JsonResponse(response)


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to Opt Out API")
