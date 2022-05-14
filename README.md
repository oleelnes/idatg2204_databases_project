# IDATG2204_2022_group12

### Group project IDATG2204

### Group 12

### Members
- Andreas Blakli
    - email: andrbl@stud.ntnu.no
- Anders Brunsberg Mariendal
    - email: anderbm@stud.ntnu.no
- Ole Kristian Elnæs
    - email: olekel@stud.ntnu.no

# Versions
- Milestone 1
- Milestone 2
- Milestone 3
- Milestone 4 - Final release

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


# How to run
git clone this repo.  
Create a virtual python enviorment; See Assignment_3 in blackboard for setup instructions.  
See reqirements.txt and install the required modules.  
Start mysql server, if using xammpp click start all.  
Create a new db named **idatg2204_2022_group12** with utf8mb4_danish_ci in phpmyadmin.  
Import the **idatg2204_2022_group12.sql** file located in the folder *sql_database*.  
Run main.py in normal "mode" not debugging mode. 

## Default 127.0.0.1:5000 GET request
Prints out all of the available endpoints.

## Public endpoint
For public endpoint with all models use this uri: *127.0.0.1:5000/public*  
For public endpoint with model search parameter use this uri: *127.0.0.1:5000/public?modelname=*  
For public endpoint with model search parameter use this uri: *127.0.0.1:5000/public?size=*
For public endpoint with model and size search parameters use this uri: *127.0.0.1:5000/public?modelname=&size=*  

**Example output json object for the url: 127.0.0.1:5000/public?modelname=race pro&size=142**
```json
[
    [
        "race pro",
        "skate",
        142,
        "racing skies, minimum length",
        123,
        "https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg"
    ]
]
```

## Storekeeper endpoint
For the storekeeper endpoint GET method with retrieving all orders with "skis available" state use this uri: **127.0.0.1:5000/storekeeper/orders**  
or **127.0.0.1:5000/storekeeper/orders?orderid=** spesific orderid search.  
Example output:
```json
[
    [
        100000,
        1,
        300000,
        "skate",
        50,
        6150,
        "new",
        "Wed, 20 Apr 2022 00:00:00 GMT"
    ],
    etc...
]
```

**127.0.0.1:5000/storekeeper/inventoryQA POST**  
Examle input (passed QA state yes/no 1/0):
```json
{
    "inventoryid":"1",
    "QAstate":"1"
}
```

Examle output:
```json
[
    [
        1,
        3,
        "filled",
        1,
        100
    ]
]
```

**127.0.0.1:5000/storekeeper/record POST**  
Examle input:
```json
{
    "inventoryid":"1",
    "date":"2022-05-14"
}
```

Examle output:
```json
[
    [
        1,
        1,
        "Sat, 14 May 2022 00:00:00 GMT"
    ]
]
```

**127.0.0.1:5000/storekeeper/changeorder**  
Example input:
```json
{
    "orderid":"100001",
    "amount":"24",
    "date":"2022-05-14"
}
```
Example output:
```json
[
    [
        100001,
        2,
        300000,
        "skate",
        24,
        200,
        "skis available",
        "Fri, 22 Apr 2022 00:00:00 GMT"
    ]
]
```

### Customer rep endpoint
For customerrep endpoint GET method with all models use this uri: *127.0.0.1:5000/customerrep/orders*  
For customerrep endpoint GET method with search parameter use this uri: *127.0.0.1:5000/customerrep/orders?state=*  
For customerrep endpoint PATCH method with with parameters orderid and state this uri: *127.0.0.1:5000/customerrep/setorderstatus?orderid=**NUMBERHERE**?state=**STATEHERE***  
For customerrep endpoint PATCH method with json object use this uri: *127.0.0.1:5000/customerrep/setorderstatus'
 ```json
 example json object for customerrep/setorderstatus: 
 {
    "orderid": "1",
    "state": "open"
}
```
If state is set to "ready to be shipped" a transport request will be created.  



## Productionplanner endpoint
For the production planner endpoint use this uri with POST request: *127.0.0.1:5000/productionplanner*  
```json
 example json object for production/planner: 
{
    "startweek":"7",
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

## Customer endpoint

## Transport endpoint
**127.0.0.1:5000/transport/orderinfo GET**  
Works with and without input!  
Example input:
```json
{
    "orderid":"100002"
}
```
Example output:
```json
[
    [
        100002,
        8,
        300000,
        "skate",
        8,
        8900,
        "ready to be shipped",
        "Sat, 23 Apr 2022 00:00:00 GMT"
    ]
]
```

**127.0.0.1:5000/transport/orderstatus PATCH**  
Example input:
```json
{
    "orderid":"100000",
    "state":"ready for pickup"
}
```
Example output:
```json
[
    [
        7080800,
        100000,
        "best ski stores",
        "heidalsvegen 3",
        "Wed, 20 Apr 2022 00:00:00 GMT",
        "ready for pickup",
        "heidis transport AS",
        400000
    ]
]
```




## Authentication endpoint
