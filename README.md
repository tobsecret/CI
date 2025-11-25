# CI
Collection of CI workflows for python repos.

### Current features
* pytest for automated testing on pull request
* ruff for linting
* mypy for typechecking

All of these run in docker containers which are built based on changes to the `Dockerfile` or `pyproject.toml`. 

Every workflow begins with checking if the appropriate image already exists on the registry and if it doesn't it's built and uploaded. This makes it robust to deleting unused images on your registry since they are rebuilt as needed. Currently uses `quay.io` for storing images since it's free if the images are public.

### Setup
1. Create a new git repo. I'll refer to its name as `<name of your repo>` and to its URL as `<repo URL>`
2. ```git clone https://github.com/tobsecret/CI.git && mv CI <name of your repo> && cd <name of your new repo> && mv CI <name of your repo>```
3. ```rm -rf .git && git init -b main```
4. `git remote add origin <repo URL> && git push -u origin main`
5. Create a `quay.io` account and password, and a quay organization
6. Set up the following variables and secrets on your repo
   * Variables
     * QUAY_ORG 
   * Secrets
     * QUAY_USER
     * QUAY_PASSWORD


### Next feature TODO
* fast CLI setup with cookiecutter template
* setup that can use org variables rather than repo variables so you can set up org variables once and be set

### Next documentation TODO
* image guide for setting up the github variables and the quay.io account