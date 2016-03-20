#TREC Evaluator

This is a django webapp to perform search comparison magic

##Steps to setup

1. mkvirtualenv --system-site-packages [env_name] && workon [env_name]

2. In a directory, call git clone https://github.com/gaftra/trec_evalutor.git. This will create a folder structure of trec_evalutor/[repo_contents]

3. pip install -r requirements.txt

4. Create a test database using python manage.py migrate 

5. Create a database superuser via python manage.py createsuperuser

6. To seed the data use the following commands:
   
   ```
      python populate_trecapp.py 
      
   ```

6. run python manage.py runserver, and navigate to 127.0.0.1:8000/trecapp

##Contributors
----------------------------
gaftra: Stephen Brown 1106679B

juranec: Daniel Juranec 2145171J

kristinagenova: Kristina Genova 2145921G

<'githubID>: Dominykas Vytautas Jakstonis <'number>
