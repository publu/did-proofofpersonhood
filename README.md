# Django Example

This project demonstrates use of verifiable credentials and presentation  for an
application.

## Dependencies

- Rust ([installation instructions](https://www.rust-lang.org/tools/install))
- Python 3
- Pip

```bash
$ sudo apt update
$ sudo apt install -y python3.6 python3-pip
```

### Python dependencies

- didkit
- Django

```bash
$ python3 -m pip install django didkit
```

## Running

For the first time running you will need to run the migrations,
this can be accomplished by running the following command:

```bash
$ touch db.sqlite3
$ python3 manage.py migrate
```

To start the server just run:

```bash
$ python3 manage.py runserver
```

To run the verification server, run the following commands under the `verifier/`
directory:
```bash
$ npm install
$ npm run dev
```

## Verifying the Credentials

You can use the verifier application by uploading a `.json` file.

`didkit-cli` is also an option:

```bash
$ didkit vc-verify-credential -p assertionMethod < vc.json
=======
# Term Definition for `gitCoinTrustBonus`

This section on line 32 in `didkit_django/issue_credential.py` should be revised,
the `@id` property should point to an URL with details about the 
[term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for
`gitCoinTrustBonus` that the user might want to check out.

```json
"gitCoinTrustBonus": {
  "@id": "https://gitcoin.co/gitCoinTrustBonus",
  "@type": "https://schema.org/Float"
}
```
