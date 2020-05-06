### Raymond's Section
- Researched sentence similarity, semantic sentence generation (chatbots, GPT-2, etc) to get ideas for metrics
  - However, scrapped i
- Finished cosine similarity work. Model is completed and notes added
- Last class tonight so should be able to devote more time to this. Tentative pair programming session for Thursday 5/7

### Raymond's TODO
- Make graphs of student dataset to get an idea of what output should look like
- Make functions that take in http endpoint, download data, and then do interpretations. Example below:

def process(download_link, result_link): # Potential improvement of having correlation and similarity analysis done on different workers. Will download file twice but scale better
    file = download(download_link) # Pulls from publisher (like S3 bucket)
    correlation_result = run_correlation(file)
    similarity_result = run_similarity(file)
    overall_result = process_results(correlation_result, similarity_result)
    update_server(result_link) # Will send POST request. Pending address to send to

### Matt's Section
* Basis of querying a CSV file is done
  * Slow
  * Not sure exactly how to filter
  * Had conversation about whether or not to filter
    * Action item: Manually create some graphs that we think will work. Do they need filte
rs? Are the x,y axis enough?
* Download CSV done
  * Uses Auth0's oauth verification to get to  * The way this is authenticated and prevented on the frontend is silly, as long as an authorized user uses JWT to login, it is accessible. If it's just logged in via session, the endpoint won't work. This is how I hope it to work but I'm not sure if this will apply wh
en building an application in React/Vue
 * Should start working on the job queuing system. Whether or not that's via Rabbitmq, Kaf
ka, or just use Redis with something managing it.
 * After that,w ork more on frontend to get a better idea of how we need to query backend
