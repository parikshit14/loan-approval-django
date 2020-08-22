#LOAN APPROVAL USECASE

*    This is a django web-api having machine learning as backend algorithm.
*    Creating a new Django project
*    Inside it create a Django app
*    The main project folder will contain the app, a folder with the same name as the project,  and a __manage.py__ file
*    We have to create a new folder in this where the model is stored in a pickled format
*    The main files that are edited are: __views.py__, __urls.py__, __settings.py__, and __HTML__ file
*    __views.py__ file deals with the backend part i.e loading the model, obtaining the values of the features used for determining the output.
*    __urls.py__ file deals with URLs i.e. linking both __views.py__ and __HTML__ files together
*    In __settings.py__ we must add the Django app name we used and the template under there respective places.
*    __HTML__ file describes the UI of the webpage we hosted.
*    The inputs entered by the user is then transferred to the __views.py__ file and the outcome is brought from there.

#### the project is deplyed on heroku
You can find the link here: [loan-approval](https://ml-loan-approval-api.herokuapp.com/)
values are set to default, one can try mix-and-match with these values to recieve different results.
