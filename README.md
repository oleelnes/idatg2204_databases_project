# IDATG2204_2022_group12

Group project IDATG2204

### Members
- Andreas Blakli
    - email: andrbl@stud.ntnu.no
- Anders Brunsberg Mariendal
    - email: anderbm@stud.ntnu.no
- Ole Kristion Elnæs
    - email: olekel@stud.ntnu.no

# Milestone 1
## Conceptual and logical models
For assumptions and models see the file **models_and_assumptions_v0.1.pdf** in the folder *documentation/models*.  
For conceptual model see the folder *documentation/models/conceptual_model*.  
For logical model see the folder *documentation/models/logical_model*.  

# Milestone 2
For SQL database see the file **idatg2204_2022_group12.sql** in the folder *sql_database*.  
For public endpoint functionality see the file **main.py** in the folder *src*. 

# Milestone 3
For SQL database see the file **idatg2204_2022_group12.sql** in the folder *sql_database*.
For Customer rep endpoint functionality see the file **main.py** in the folder *src*.

## Note:
See the issue tracker for spesific details regarding work and priorities and Milestones under the Issues sidebar.  
https://git.gvk.idi.ntnu.no/course/idatg2204/idatg2204-2022-workspace/andrbl/idatg2204_2022_group12/-/issues?scope=all&state=all

# Versions
- v0.1 - Milestone 1
- v0.2 - Milestone 2
- v0.3 - Milestone 3

# How to run
git clone this repo.  
Create a virtual python enviorment; See Assignment_3 in blackboard for setup instructions.  
See reqirements.txt and install the required modules.  
Start mysql server, if using xammpp click start all.  
Import the **idatg2204_2022_group12.sql** file located in the folder *sql_database* into phpmyadmin and name it **idatg2204_2022_group12.sql**.  
Run main.py in normal "mode" not debugging mode. 

## Public endpoint
For public endpoint with all models use this uri: *127.0.0.1:5000/public*  
For public endpoint with model search parameter use this uri: *127.0.0.1:5000/public?modelname=*

## Customer endpoint

## Customer rep endpoint
For customerrep endpoint GET method with all models use this uri: *127.0.0.1:5000/customerrep/orders*  
For customerrep endpoint GET method with search parameter use this uri: *127.0.0.1:5000/customerrep/orders?state=*  
For customerrep endpoint POST method with with parameters orderid and state this uri: *127.0.0.1:5000/customerrep/order?orderid=**NUMBERHERE**?state=**STATEHERE***  
For customerrep endpoint POST method with json object use this uri: *127.0.0.1:5000/customerrep/order
 ```json
 example json object for customerrep/order: 
 {
    "orderid": "1",
    "state": "open"
}
```
If state is set to "fulfilled" a transport request will be created.  

## Storekeeper endpoint
For the storekeeper endpoint GET method with retrieving all orders with "skis available" state use this uri: *127.0.0.1:5000/storekeeper/orders*  

## Productionplanner endpoint
For the production planner endpoint use this uri with POST request: *127.0.0.1:5000/productionplanner*  
```json
 example json object for production/planner: 
{
    "month":"7",
    "productid": "1",
    "day": "1",
    "type": "test",
    "productionAmount": "12"
}

expected output:
[
    [
        56,
        29,
        1,
        1,
        "test",
        12
    ],
    etc...
]
```
