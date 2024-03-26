import asyncio
import aiohttp
import json
from uuid import uuid4


async def fetch_job(session, url):
    """Asynchronously fetches a job detail from the given URL."""
    async with session.get(url) as response:
        # Assuming the service response is a well-formed JSON
        response_json = await response.json()
        return response_json['jobid']


async def main():
    urls = [f"https://someurl/getjobdetails/id/{uuid4()}" for _ in range(1000, 2001)]
    # Using a set to ensure uniqueness of job ids
    job_ids = set()

    async with aiohttp.ClientSession() as session:
        # Prepare and dispatch all requests concurrently
        tasks = [fetch_job(session, url) for url in urls]
        # Wait for all tasks to complete and collect results
        for future in asyncio.as_completed(tasks):
            job_id = await future
            job_ids.add(job_id)

    # Preparing the final JSON output
    output = {"jobs": list(job_ids)}
    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    asyncio.run(main())
