dev:
	dev_appserver.py app

uat:
	appcfg.py --version uat --noauth_local_webserver -A hot-zones update app/

prod:
	appcfg.py --version prod --noauth_local_webserver -A hot-zones update app/