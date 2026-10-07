from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_GET


@require_GET
def status(request):
    """Simple health-check endpoint: GET /api/status/"""
    return JsonResponse(
        {
            "status": "online",
            "message": "I am online",
            "timestamp": timezone.now().isoformat(),
        }
    )
