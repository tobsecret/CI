# CI
Collection of CI workflows for python repos.

### Current features
* pytest for automated testing on pull request
* ruff for linting
* mypy for typechecking

All of these run in docker containers which are built based on changes to the `Dockerfile` or `pyproject.toml`. 

Every workflow begins with checking if the appropriate image already exists on the registry and if it doesn't it's built and uploaded. This makes it robust to deleting unused images on your registry since they are rebuilt as needed. Currently uses `quay.io` for storing images since it's free if the images are public.

### Next feature TODO
* fast setup with cookiecutter template
* setup that can use org variables rather than repo variables so you can set up org variables once and be set

### Next documentation TODO
* image guide for setting up the github variables and the quay.io account