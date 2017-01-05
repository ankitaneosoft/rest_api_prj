from fabric.api import local, settings, run, cd

def prepare_deploy():
    local("./manage.py test quickstart")
    local("git add -A && git commit -m 'deploying changes'")
    local("git push")


def deploy():
    code_dir = '/home/neosoft/Demo'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone https://github.com/ankitaneosoft/rest_api_prj.git %s" % code_dir)
    with cd(code_dir):
        run("git pull origin master")
        run("touch app.wsgi") 