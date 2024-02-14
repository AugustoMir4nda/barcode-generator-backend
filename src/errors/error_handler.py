from src.views.http_types.http_response import HttpResponse

#todos os erros são tratados como objetos vindo da exception
def handle_errors(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code = 500,
        body = {
            "errors": [{
                "title":"Server Error",
                "detail": str(error)
            }]
        }
    )