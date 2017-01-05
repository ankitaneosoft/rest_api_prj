from fabric.api import local, settings, run, cd,sudo

def prepare_deploy():
    local("tutorial/manage.py test quickstart")
    local("git add -A && git commit -m 'deploying changes'")
    local("git push")


def deploy():
	owner = 'root'
	code_dir = '/home/neosoft/Demo'
	with settings(warn_only=True):
		if run("test -d %s" % code_dir).failed:
			run("git clone https://github.com/ankitaneosoft/rest_api_prj.git %s" % code_dir)
	with cd(code_dir):
		run("git pull origin master")
		run("touch app.wsgi")
		code_dir = '/home/neosoft/Demo'
		with cd(code_dir):
			#venv_command = 'source ../bin/activate'
			pip_command = 'pip install -r requirements.txt'
			#sudo('%s && %s' % (venv_command, pip_command), user=owner)
			sudo('%s' % pip_command, user=owner)
			south_command = 'python tutorial/manage.py migrate --all'
			run_command = 'python tutorial/manage.py runserver'
			sudo('%s && %s' % (venv_command, run_command), user=owner)
			#sudo('%s' % south_command, user=owner) 