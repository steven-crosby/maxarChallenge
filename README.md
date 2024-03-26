# PROBLEM

A program is needed to issue between 1000 and 2000 REST requests to a single endpoint to collect a set of unique identifiers.  The identifiers returned from the REST call are JOB Id's of another system that can be tracked later.  The program must issue all the requests and return at exit a JSON output that is the list of JOB identifiers as returned from the REST call. It is expected that the REST calls will respond within a random distribution of 1 - 10 seconds.

- Preferably Java or Python
- Use any available libraries to your advantage 
- The completed challenge must be pushed to GitHub (github.com) and accessible for review 
- Include relevant documentation for the running and testing of the app 
- It’s ok if you are unable to complete the challenge, but at minimum please document possible implementation steps and include a to-do list. 

## Requirements List

1. Must make 1 to 2 thousand REST calls to a single REST endpoint as efficiently as possible to collect the JOB Id's.
2. Format of the REST call will be GET 
3. REST call will include the URL parameter called id
4. Each REST call will be issued with a different value assigned to the id parameter 
5. Expected Responses from the REST call will take between 1 and 10 seconds and will be random in nature.
6. The REST response format will be well formatted JSON.
7. The REST response format will have one key value pair with the key called "jobId" and the value being a generated UUID.
8. All response must be collected and stored for a final response at program exit.
9. At program exit a well formatted JSON object will be print for analysis.
10. The JSON package on exit must have a key value pair with the key being 'jobs' and the value being a JSON List of the response job id's values from the REST calls made.

## SOLUTION

1. Setup and Initialization: se the `aiohttp` library for async HTTP requests. Make sure it's installed in your environment.
2. Asynchronous REST Calls: The program will make use of async functions to send GET requests to the specified endpoint. Each call will be made with a unique `id` parameter.
3. Collecting and Storing JOB IDs: Responses will be parsed to extract the `jobid`, which will then be stored in a list.
4. Outputting the Results: After all requests have been made and responses collected, the program will output a JSON object containing all the `jobid`s collected.

### Explanation and Logic:

- Asynchronous Execution: The use of `asyncio` and `aiohttp` allows the program to send and manage multiple HTTP GET requests concurrently. This is crucial for efficiently handling 1000 to 2000 requests, especially given the random response time of 1 to 10 seconds per request.
- Unique Job ID Collection: A set is used to store job IDs to automatically ensure uniqueness. Since the task requires collecting unique identifiers, any duplicate `jobid` returned by the REST endpoint will not be added twice.
- **Flexible Request Generation**: The code dynamically generates URLs with unique `id` parameters using `uuid4()`. This meets the requirement that each REST call is issued with a different value assigned to the `id` parameter.
- JSON Output: On exit the program formats the collected job IDs into a JSON object and prints it. This JSON object contains key value pair with the key being 'jobs' and the value being a JSON List of the response job id's values from the REST calls made.