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

