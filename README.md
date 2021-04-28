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
$ python3 -m pip install django
```

### Building DIDKit

DIDKit is used to handle credentials and presentations, since it's not yet
publically available in PyPI manual installation is required.

To do so got to the root folder of this repository and run:
```bash
$ make -C lib install-python
```

For the verifier the `node` version of the library also needs to be built:
```bash
$ make -C lib ../target/test/node.stamp
```

Then you will have to link it using `npm`

On the library directory (`didkit/lib/node`) run:
```bash
$ npm link
```

And then, on the verifier directory (`popp-demo/verifier`) run:
```bash
$ npm link didkit
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
```
