Quickstart
----------

Deployment with Docker
----------------------

You must have ``docker`` and ``docker-compose`` tools installed to work with material in this section.
First, create ``.env`` file like in `Quickstart` section or modify ``.env.example``.
``POSTGRES_HOST`` must be specified as `db` or modified in ``docker-compose.yml`` also.
Then just run::

    docker-compose up -d app

Application will be available on ``localhost`` in your browser.

Web routes
----------

All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.


Project structure
-----------------

Files related to application are in the ``app`` or ``tests`` directories.
Application parts are:

::

    app
    ├── api              - web related stuff.
    │   ├── dependencies - dependencies for routes definition.
    │   ├── errors       - definition of error handlers.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── db               - db related stuff.
    │   ├── migrations   - manually written alembic migrations.
    │   └── repositories - all crud stuff.
    ├── models           - pydantic models for this application.
    │   ├── domain       - main models that are used almost everywhere.
    │   └── schemas      - schemas for using in web routes.
    ├── resources        - strings that are used in web responses.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.

Poetry
------

## Installation

Poetry provides a custom installer that will install `poetry` isolated
from the rest of your system by vendorizing its dependencies. This is the
recommended way of installing `poetry`.

### osx / linux / bashonwindows install instructions
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
### windows powershell install instructions
```bash
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```
Alternatively, you can download the `get-poetry.py` file and execute it separately.

The setup script must be able to find one of following executables in your shell's path environment:

- `python` (which can be a py3 or py2 interpreter)
- `python3`
- `py.exe -3` (Windows)
- `py.exe -2` (Windows)

If you want to install prerelease versions, you can do so by passing `--preview` to `get-poetry.py`:

```bash
python get-poetry.py --preview
```

Similarly, if you want to install a specific version, you can use `--version`:

```bash
python get-poetry.py --version 0.7.0
```

Using `pip` to install `poetry` is also possible.

```bash
pip install --user poetry
```

Be aware, however, that it will also install poetry's dependencies
which might cause conflicts.

## Updating `poetry`

Updating poetry to the latest stable version is as simple as calling the `self update` command.

```bash
poetry self update
```

If you want to install prerelease versions, you can use the `--preview` option.

```bash
poetry self update --preview
```

And finally, if you want to install a specific version you can pass it as an argument
to `self update`.

```bash
poetry self update 1.0.0
```

*Note:*

    If you are still on poetry version < 1.0 use `poetry self:update` instead.

## Creating new project

```bash
poetry new <project-name>
```

## Initialising a pre-existing project

```bash
cd pre-existing-project
poetry init
```

## Specifying dependencies
from pypip depedencies
```bash
poetry add <repo-name>
```
from private depedencies
```bash
poetry add git+ssh://git@stash.gdn-app.com:7999/perftm/git-and-pip.git
```

Alembic
-------

## Installation
```bash
poetry add alembic
```

## Initialization
```bash
poetry run alembic init <migrations>
```

## Autogenerate migration script
```bash
poetry run alembic revision --autogenerate -m "<message>"
```

## Execute migration script
```bash
poetry run alembic upgrade head
```