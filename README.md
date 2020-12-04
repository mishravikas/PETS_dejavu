
# Déjà vu: Abusing Browser Cache Headers to Identify and Track Online Users
Paper to appear at PETS '21 by Vikas Mishra, Pierre Laperdrix, Walter Rudametkin and Romain Rouvoy

# Instructions
- Clone the repo

- Install virtualenv
```bash
    pip install virtualenv
    virtualenv --help
```
    
- Create and activate a virtualenv
```bash
	virtualenv dejavu
	source dejavu/bin/activate
```

- Install requirements
```bash
	pip install -r requirements.txt
```

-  Start the demo server from the root of the repo
```bash
	python manage.py runserver
```
- The PoC includes a sample resource and more can be added from the admin panel which can be accessed at http://localhost:8000/admin with username as `admin` and password as `dejavupets`
This PoC includes both tracking and history sniffing demos and both can be tested by visiting
http://localhost:8000 and following the instructions mentioned on the page.



