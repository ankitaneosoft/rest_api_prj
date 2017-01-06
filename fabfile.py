from fabric.api import local, settings, run, cd,sudo,env
#either define this or system will prompt for ip.
env.hosts = ['10.0.30.109']

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
			v_env_command = 'virtualenv Djangoproject'
			v_actv_command = 'source Djangoproject/bin/activate'
			sudo('%s && %s' % (v_env_command, v_actv_command),user=owner)
			pip_command = 'pip install -r requirements.txt'
			sudo('%s' % pip_command, user=owner)
			south_command = 'python tutorial/manage.py migrate'
			run_command = 'python tutorial/manage.py runserver 10.0.30.109:8000'
			sudo('%s && %s' % (south_command, run_command), user=owner)


