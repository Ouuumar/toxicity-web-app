# Toxic web app


### Short web application to analyze your sentence toxicity

<br>

How to run it ? :

    - Go on your beloved command prompt (as admin if it's possible)
    - Be sure to have a Docker instance running
    - Run the following command : docker-compose up

<br>

Go on your local host, mapping port 7979 :

    - http://localhost:7979

<br>

**Then, write whatever sentence you want, click on the submit button, and discover it's toxicity !**

##### (IT TAKES TIME to process the request ... be patient)

____________________________________________________________

<br>

When you are done, properly delete containers if it's necessary :
    
    - Run the following command : docker-compose down

You can also run images, and run test separtly

test :  - cd ./tests
        - python3 tests.py
        
You can build images for the tests and the app

    - cd to the folder api or tests.

    - docker build -t toxic .
    - docker run -dp 7979:7979 toxic

Same steps for the tests

