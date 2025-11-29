# Circuit Breaker Labs Python Client

## Usage

First, create a client:

```python
from circuit_breaker_labs import Client

client = Client(base_url="https://api.circuitbreakerlabs.ai/v1/")
```

Now call your endpoint and use your models:

```python
import os

from circuit_breaker_labs.api.evaluations import evaluate_system_prompt_post
from circuit_breaker_labs.models import EvaluateSystemPromptRequest

with client as client:
    request = EvaluateSystemPromptRequest(
        0.5,
        3,
        2,
        os.getenv("SYSTEM_PROMPT"),
        "anthropic/claude-3.7-sonnet",
    )

    run_tests_response = evaluate_system_prompt_post.sync(
        client=client,
        cbl_api_key=os.getenv("CBL_API_KEY"),
        body=request,
    )
```

Or do the same thing with an async version:

```python
import os

from circuit_breaker_labs.api.evaluations import evaluate_system_prompt_post
from circuit_breaker_labs.models import EvaluateSystemPromptRequest

async with client as client:
    request = EvaluateSystemPromptRequest(
        0.5,
        3,
        2,
        os.getenv("SYSTEM_PROMPT"),
        "anthropic/claude-3.7-sonnet",
    )

    run_tests_response = evaluate_system_prompt_post.asyncio(
        client=client,
        cbl_api_key=os.getenv("CBL_API_KEY"),
        body=request,
    )
```

Things to know:

1. Every path/method combo becomes a Python module with four functions:
   1. `sync`: Blocking request that returns parsed data (if successful) or `None`
   1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
   1. `asyncio`: Like `sync` but async instead of blocking
   1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `circuit_breaker_labs.api.default`

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from circuit_breaker_labs import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://api.circuitbreakerlabs.ai/v1/",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from circuit_breaker_labs import Client

client = Client(
    base_url="https://api.circuitbreakerlabs.ai/v1/",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://api.circuitbreakerlabs.ai/v1/", proxies="http://localhost:8030"))
```
