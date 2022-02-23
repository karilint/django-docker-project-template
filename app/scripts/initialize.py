import os
from django.contrib.auth.models import User
#from allauth.account.models import EmailAddress
from django.contrib.sites.models import Site

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'password')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
site_name = os.environ.get('SITE_NAME', 'Website Name')
site_domain = os.environ.get('SITE_DOMAIN', 'localhost:8000')

if not User.objects.filter(username=username).exists():
    print('CREATING DJANGO SUPERUSER')
    print(f'Username: {username}')
    print(f'Password: {password}')
    print(f'Email: {email}')
    user = User.objects.create_user(username, email, password,
                                    is_superuser=1, is_staff=1)
#    EmailAddress.objects.create(
#        user=user, email=user.email, verified=1, primary=1)
else:
    print('DJANGO SUPERUSER ALREADY EXISTS')
    print(f'Username: {username}')

site = Site.objects.get(id=1)
if not (site.name == site_name and site.domain == site_domain):
    print('UPDATING DJANGO SITE')
    print(f'Name: {site_name}')
    print(f'Domain: {site_domain}')
    Site.objects.filter(id=1).update(name=site_name, domain=site_domain)
else:
    print('DJANGO SITE UP TO DATE')
