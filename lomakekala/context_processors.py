def lomakekala_context(request):
    from django.conf import settings

    vars = dict(
        settings=settings,
    )

    return vars
