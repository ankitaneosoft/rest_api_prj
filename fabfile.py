from fabric.api import local, settings, run, cd,sudo,env
#either define this or system will prompt for ip.
from fabric.network import ssh_config

#env.hosts = ['neosoft@10.0.30.109']
env.hosts = ['webwerks@10.0.8.104','neosoft@10.0.30.109']


def prepare_deploy():
    local("git add -A && git commit -m 'deploying changes'")
    local("git push")


def deploy():
	owner = 'root'
	code_dir = 'ank_code'
	with settings(warn_only=True):
		if run("test -d %s" % code_dir).failed:
			dir_command = 'mkdir ' + code_dir
			chmod_command = 'chmod 777 ' + code_dir
			sudo('%s && %s' % (dir_command,chmod_command), user=owner)
			#sudo('%s' % dir_command, user=owner)
			run("git clone https://github.com/ankitaneosoft/rest_api_prj.git %s" % code_dir)
	with cd(code_dir):
		run("git pull origin master")
		v_env_command = 'virtualenv Djangoproject'
		v_actv_command = 'source Djangoproject/bin/activate'
		sudo('%s && %s' % (v_env_command, v_actv_command),user=owner)
		pip_command = 'pip install -r requirements.txt'
		sudo('%s' % pip_command, user=owner)
		south_command = 'python tutorial/manage.py migrate'
		run("touch app.wsgi")
		run_command = 'python tutorial/manage.py runserver'
		sudo('%s && %s' % (south_command, run_command), user=owner)



