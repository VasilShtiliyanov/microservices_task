This is a project for associating job titles with categories and questions for a job interview. The project is developed
using the Microservices architectural pattern and Django REST Framework.

Version Control:
    $ Python 3.6
    $ Django 2.1

Steps to start the project::

    $ git clone https://github.com/VasilShtiliyanov/emoovtask.git

    $ Create a virtual environment using python3.6

    $ Inside the virtual environment: pip install -r requirements.txt

    $ Start project "jobtitle" on default port (8000) and project "question" on port 8001!

    $ Run (for both projects) - python manage.py makemigrations -> python manage.py migrate

    $ Create some objects in the databases of both projects


I have decided to use a simple Request/Response pattern for the ISC between the projects since I have only two microservices.
For more microservices I would have used the Pub/Sub Pattern provided by either RabbitMQ or Django Channels and Daphne

The available requests for the projects are as follows::
    $ http://127.0.0.1:8000/job/job -> GET request where you can either pass a parameter(job_title) to get a specific job,
    with all categories related to the job and all questions related to the category, or get all job titles with all categories related to them.

    $ http://127.0.0.1:8000/job/post -> POST request for creating a job, and a category for it. Parameter map is:
        'job_title'
        'name'
        'desc'

