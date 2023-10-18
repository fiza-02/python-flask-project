# flask-hands-on
To run a flask application 

Before we run a application we need to set an environment variable to the file that need to be our flask application.

windows powershell

```python
set FLASK_APP=hello.py
$env:FLASK_APP = "hello.py"
flask run
```

linux/mac

export FLASK_APP = flaskblog.py

flask run ⇒ to run the application

to track the changes run in debug mode ⇒ export FLASK_DEBUG =1
To enable debug mode, use the --debug option.

$ flask --app hello run --debug
 * Serving Flask app 'hello'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn

without restarting the web server the changes will reload automatically.
# Error while running a flask application
 * Serving Flask app 'flaskblog.py'
 * Debug mode: off
An attempt was made to access a socket in a way forbidden by its access permissions
This error occurs when port is already in use
to run application with change in hostname and port 
flask run -h localhost -p 3000

- Templating engine python uses jinja2

- Template Inheritance 
 - combine the same code in html
 - Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.