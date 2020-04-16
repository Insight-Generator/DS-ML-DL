We want to create an application which can take in CSVs files uploaded and use a model to get noteworthy columns and create graphs from the data.

### Proposal
We have a model that is able to take in CSV files and output a set of recommended types of graphs with matching fields for graphs.

We create a simple web app which:
  * Keeps track of users via an external user management system (Auth0, etc.)
  * A way for each user to upload files, storing the file in a static location
  * Queues files to some sort of workflow to process the data
  * A way to display graphs using the output of the workflow

### Schema
* Users
  * id
  * token
* Files
  * id
  * file location
  * file metadata
  * column details (jsonb)
  * timestamps
  * user relation
  * prediction status
  # version
  # version diff
* Visualization
  * id
  * file relation
  * type (of graph/chart)
    * Options:
      * Line graph
      * Bar chart
      * Pie chart
      * Histograph
      * Scatter plot
      # Heatmap
      # 95 percentile, 99 percentile, etc.
  * axis (jsonb: {x:column name, y: column name})
  * graph metadata (jsonb: Detail graph somehow, x axis start, x axis scale, y axis star, y axis scale)


#### Machine Learning Model
word embeddings

#### Keep track of users
Instead of rolling our own user system, we rely on an external user management such as Auth0. The user management system will take care of logic that deals with users and passwords for us. We will manage a token that represents the user on our end.

#### Upload files
After we receive the file, we store it on a static location. To save money and complexity, this can just live on the local filesystem that is running our web application. We can write a wrapper around it so that it can easily be adapted to something like S3. We store the file endpoint in our database.

#### Queue processes
We will build a typical pub/sub system, leveraging RabbitMQ and celery(?) to run our jobs.
After we have stored the file, we will add an entry to our queue.
Our subscriber will read from the queue, processing an entry at a time. This will run our model against the data input and then write the output to the database. Perhaps this will also add to another queue to generate graphs.

MVP:
Process to get columns name and input into model

Future:
Use data in file: count of rows, repeating values, empty data, etc. to factor into graph prediction

#### Display graphs
With the output of our model, we will need to create a graph. What we will do is load the file's columns and manipulate them into graphs via d3.js. If the file is too big, too bad for our MVP :p

The alternative is to generate the graphs as a PDF of some sort after our model runs. If that's the case, we just upload the file similar to how we handle our static files and then return them to the user that way. We can also then delete the origin data.
