# LogApp-RESTful-API

I was tasked with creating a RESTful API that could consume, store and process logs from the user/frontened application, and to make these logs retrievable for batch processing.
These logs should be retrievable by quering the logs based on: User, date range or log type.

I made use of the Flask framework, where my files and packages are coded in Python. SQLAlchemy was utilised as the app's object relational mapper. An SQLlite database was initialized
with the following tables: logs, actions and properties. Every log has a session ID. Therefore, the variable sessionId was used as a foreign key to link the three tables. 

**REST API DOCUMENATION:**

***app.py:***

The REST API is run using this file. It contains the various endpoints needed to satisfy how the logs should be stored and retrieved. The app runs locally at http://127.0.0.1:5000/

*api.add_resource(Log, '/log/<string:name>')*
-this endpoint takes in the a log and stores the information in the relevant database columns.

*api.add_resource(Date, '/date')*
-this endpoint takes in a start and end date and returns all logs that fall within that date range.

*api.add_resource(Type, '/type/<string:name>')*
-this endpoint takes in the type of action and returns all logs in which that action occured.

*api.add_resource(UserId,'/id/<string:name>')*
-this endpoint takes in a userId and returns all logs assocaited with that user



***db.py:***

Initializes SQLAlchemy

**PACKAGES - models and resources**

**models**

*The models package contains the files neccesary to create the database models and relate these objects to the database.*

-**models.logs** initializes the LogModel model. This model has various functions such as finding a log by sessionId (*models.log.LogModel.find_by_name(name)*),
finding logs by user (*model.log.LogModel.find_by_user(userId)*) and saving the details to the database (*models.log.LogModel.save_to_db()*).

-**models.actions** initializes the actionsModel model. This model has various functions such as finding a log by date (*models.actions.actionsModel.find_by_date(start_date,end_date))*,
and saving the details to the database (*models.actions.actionsModel.save_to_db()*).

-**models.properties** initializes the propertiesModel model. This model has various functions such as finding a log by action type (**models.properties.propertiesModelModel.find_by_type(Type))**,
and saving the details to the database (*models.properties.propertiesModel.save_to_db()*).

**resources**

*The resources package contains the files neccesary to create the resource classes needed for the various API endpoints.*

-**resources.log**  contains the classes needed to store the logs and retrieve the logs by either sessionId or User Id. 
*resources.log.Log* allows for both GET and POST requests. The POST request is used to store the log info into the database and the GET request is used to retrieve the logs by their session Id.
*resorces.log.UserId* allows for a GET request. The GET request is used to retrieve logs by user Id.
*resources.log.LogList* allows for a GET request. The GET request is used to retrieve all logs.

-**resources.action** contains the classes needed to retrieve logs by either a date range or action type.
*resources.action.Date* allows for a GET request. The GET request takes in two dates and is used to retrieve all logs that fall within and including these dates.
*resources.action.Type* allows for a GET request. The GET request takes in the type of action and is used to retrieve all logs in which that action occured.

**MAKING THIS LOG API SCALABLE:**

In order to make this API scalable, I'd make use of cloud-based technologies. Powerful servers can be used to manage the load required. These servers can also be automated to decrease or
increase in amount depending on the amount of requests incoming. The extensive storing capabilities of cloud services also reduces the need for worrying about storing data at a local server.


