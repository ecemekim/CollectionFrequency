**Summary**:

It is written to retrieve all Bin and Operation pairs using Django Framework and PostgreSQL.
The tables in question were previously designed as one to many. The models should be modeled with `many to many` because of
one operation is to be used for more than one bin and also a bin is to be used for more than one operation. While defining 
the models in the file models.py, a new model `bin_operation` is created automatically by giving the operation model
inside the bin model with `ManyToManyField`. By making a request to this new model, access to all 
operation and bin pairs is provided.


**Steps**:

1- Run `sudo apt-get install docker` command

2- Run `sudo apt-get install docker-compose` command

3- Run `sudo docker-compose up -d --build` command when at LastPoints directory.

4- Run `curl http://0.0.0.0:8081/home/` command or get http://0.0.0.0:8081/home/ on your browser and see the result of 
all Bin and Operation pairs.

5- You can view tables with pgAdmin if you want. Get http://0.0.0.0:5051/ on your browser and login with credentialds 
from env/dev.env file. Then create server, you can find db's network ip `lastpoints_db_1` container's network settings 
and also credentials in env/dev.env file.
