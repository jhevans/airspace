from django.shortcuts import render_to_response


def radar(request):
    extra = {}

    return render_to_response('radar.html', extra)