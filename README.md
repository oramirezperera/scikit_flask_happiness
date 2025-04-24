# scikit_flask_happiness
## A project using Scikit Learn, Flask and the happiness dataset

Hi! Welcome to this project!
In this project I'll Implement a model to predict the score on a country using the World Happiness Report

To use this project you need to follow the following steps:

## 1 
Have Python and Git Installed in your PC

## 2

### Clone the project

in your terminal run
```
git clone <the url of this project>
```

## 3
Create a Python virtual environment.
For this you can use the following examples:

### 3.1
If you are using python
```python
python -m venv <the_name_of_you_environment>
```

Tipycally 
the virtual environment is called venv or env in this situations
Then activate your environment
On Linux
```bash
source <the_name_of_you_environment>/bin/activate
```
On windows
```
<the_name_of_you_environment>\scripts\activate
```

After you finished using the project you can deactivate it using
```
deactivate
```

### 3.2
If you are using conda you can use
```
conda create --name <environment_name>
```
Then activate the environment calling

```
conda activate <environment_name>
```

## 3
Install the pre-requisites for Python to run the project
To do this you can use

```python
pip install -r requirements.txt
```

## 4 
Then run 
```
python3 server.py
```

Now you will have the server running

## 5
Open your browser and type 
```
http://localhost:8080/predict_all
```

You will get an image as this one
insert image here

## 6 
The image shows you the country, the score from the dataset,  and the score predicted by our model
