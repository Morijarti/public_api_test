from django.http import JsonResponse
from opt_out.public_api.api.models import Submission


def submit(request):
    item = Submission()

    item.url = request.POST["urls"]

    item.save()
    response = {"submission_id": item.submission_id}
    return JsonResponse(response)
