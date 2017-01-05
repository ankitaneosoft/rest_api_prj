from fabric.api import local

def prepare_deploy():
    local("./manage.py test quickstart")
    local("git add -A && git commit -m 'deploying changes'")
    local("git push")