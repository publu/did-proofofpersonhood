from python_django.settings import KEY_PATH
from django.core.files import File
from datetime import datetime, timedelta
import didkit
import json
import uuid


def issueCredential(request):
    with open(KEY_PATH, "r") as f:
        key_file = File(f)
        key = json.loads(key_file.readline())
    key_file.close()

    location = request.META.get("HTTP_X_LOCATION", "/didkit/")
    didWeb = "did:web:" + \
        request.META["HTTP_HOST"] + \
        ':'.join(location[:-1].split('/'))
    subject = request.POST.get('subject_id').__str__()
    gitCoinTrustBonus = float(request.POST.get('gitCoinTrustBonus')).__str__()
    issuance_date = datetime.utcnow().replace(microsecond=0)
    expiration_date = issuance_date + timedelta(weeks=4)

    credential = {
        "@context": ["https://www.w3.org/2018/credentials/v1"],
        "type": ["VerifiableCredential"],
        "issuer": didWeb,
        "issuanceDate": issuance_date.isoformat() + "Z",
        "expirationDate": expiration_date.isoformat() + "Z",
        "credentialSubject": {
            "@context": [{
                "gitCoinTrustBonus": {
                    "@id": "https://gitcoin.co/gitCoinTrustBonus",
                    "@type": "https://schema.org/Float"
                }
            }],
            "id":
            subject,
            "gitCoinTrustBonus":
            gitCoinTrustBonus,
        },
    }

    didkit_options = {
        "proofPurpose": "assertionMethod",
        "verificationMethod": didWeb + "#main",
    }

    credential = didkit.issueCredential(
        json.dumps(credential),
        json.dumps(didkit_options),
        json.dumps(key),
    )
    return json.loads(credential)
