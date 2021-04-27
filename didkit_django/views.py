from django.shortcuts import render
from django.http import HttpResponse
import socket
from django import forms
from django.http import JsonResponse
from didkit_django.issue_credential import issueCredential
from django.views.decorators.csrf import csrf_exempt
import json
from python_django.settings import KEY_PATH
from django.core.files import File
from uuid import uuid4


def index(request):
    location = request.META.get("HTTP_X_LOCATION", "/didkit/")
    context = {
        "url": request.META["HTTP_HOST"] + ':'.join(location[:-1].split('/')),
    }
    return render(request, "didkit_django/index.html", context)


def credential(request):
    context = {
        "credential": issueCredential(request),
    }

    return render(request, "didkit_django/credential.html", context)


def well_known(request):
    location = request.META.get("HTTP_X_LOCATION", "/didkit/")

    # generates the didweb handler
    didWeb = "did:web:" + \
        request.META["HTTP_HOST"] + \
        ':'.join(location[:-1].split('/'))

    # opens the key in order to get the public part of it
    with open(KEY_PATH, "r") as f:
        key_file = File(f)
        key = json.loads(key_file.readline())
    key_file.close()

    key_id = didWeb + "#main"
    # adds the did.json to the context
    credential = {
        "@context":
        "https://www.w3.org/ns/did/v1",
        "id":
        didWeb,
        "verificationMethod": [{
            "id": key_id,
            "type": "Ed25519VerificationKey2018",
            "controller": didWeb,
            "publicKeyJwk": {
                "kty": key["kty"],
                "crv": key["crv"],
                "x": key["x"]
            }
        }],
        "authentication": [key_id],
        "assertionMethod": [key_id],
    }
    return JsonResponse(credential)
