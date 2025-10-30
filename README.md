# Client-Server Architecture: Key Concepts

## Overview
- **Client-server architecture** is a model where multiple clients request and receive services from a centralized server.

## Components
- **Client:** Initiates requests; can be browsers, mobile apps, or scripts.  
- **Server:** Processes requests, manages resources, and sends responses.

## How It Works
1. Client sends a request to the server.  
2. Server processes the request.  
3. Server sends back a response.

## Advantages
- Centralized management of resources.  
- Scalability: Multiple clients can connect to one server.  
- Security: Easier to enforce policies and controls.

## Summary
- The client-server model is fundamental for web and API development.  
- Clients interact with servers to access resources and services.  
- Enables modular, scalable, and secure application design.

# HTTP vs HTTPS: A Python Developer's Guide

## What is HTTP?
- **HTTP (HyperText Transfer Protocol)** is the foundation of data communication on the web.  
- It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands.

## What is HTTPS?
- **HTTPS (HyperText Transfer Protocol Secure)** is HTTP with encryption.  
- It uses SSL/TLS to secure data transfer between client and server.

## Key Differences
| Feature      | HTTP                        | HTTPS                          |
|--------------|-----------------------------|--------------------------------|
| Security     | Unencrypted                 | Encrypted (SSL/TLS)            |
| Port         | 80                          | 443                            |
| URL Prefix   | http://                     | https://                       |
| Data Privacy | Vulnerable to interception  | Data is protected              |

## Components of HTTP/HTTPS
- **Client:** Usually a browser or API consumer (e.g., Python requests).  
- **Server:** Hosts resources (web pages, APIs).  
- **Request:** Sent by client (GET, POST, etc.).  
- **Response:** Sent by server (status code, headers, body).  
- **Headers:** Metadata (content type, authentication).  
- **Body:** Actual data (HTML, JSON, etc.).  
- **SSL/TLS (HTTPS only):** Protocols for encryption and authentication.

## How HTTPS Works (Simplified)
1. Client connects to server.  
2. Server presents SSL certificate.  
3. Client verifies certificate.  
4. Encrypted communication begins.

### What is an SSL Certificate?
- An **SSL certificate** is a digital certificate that authenticates a website's identity and enables encrypted communication.  
- It contains information about the website, the certificate authority (CA) that issued it, and a public key for encryption.  
- Browsers and clients use SSL certificates to verify that they are communicating with the legitimate server and to establish a secure, encrypted connection.  
- SSL certificates are essential for HTTPS and help prevent eavesdropping and tampering.

## Why Use HTTPS?
- Protects sensitive data (passwords, personal info) by encrypting communication.  
- Prevents man-in-the-middle attacks by verifying server identity.  
- Required for modern web standards; browsers warn users about insecure HTTP sites.  
- Ensures data integrity and privacy for users and applications.

## Python Example
```python
import requests

# HTTP request (not secure)
response = requests.get('http://example.com')

# HTTPS request (secure)
secure_response = requests.get('https://example.com')
```

## Summary
- Use HTTPS for security.  
- HTTP is for basic, unsecured communication.  
- HTTPS adds encryption and trust.

# Sync vs Async: Concepts, Trade-offs, and When to Use

## Synchronous (sync) processing
- A sync function runs from start to finish before returning control.  
- Blocking I/O (e.g., file read, blocking DB calls, time.sleep) halts the current thread.  
- Simpler mental model and easier debugging.  
- For CPU-bound work, use separate processes or threads (multiprocessing/threadpool).

## Asynchronous (async) processing
- Async functions (coroutines) yield control when awaiting I/O, allowing other tasks to run on the same thread.  
- Ideal for high-concurrency, I/O-bound workloads (many concurrent HTTP requests, websockets, streaming).  
- Requires non-blocking libraries/drivers (async DB drivers, async HTTP clients).  
- Runs on an event loop (e.g., asyncio).

## Trade-offs
- Async improves throughput for I/O-bound workloads but adds complexity (debugging, libraries must be async-aware).  
- Sync code is often simpler and fine for low-to-moderate concurrency or when using worker processes.  
- Mixing blocking sync calls inside async code will block the event loop unless moved to a thread/process pool.

## Practical rules
- If your handlers do mostly I/O and you need many concurrent connections, prefer async.  
- If you rely on blocking third-party libraries without async alternatives, use sync or run blocking calls in a threadpool.  
- For CPU-bound tasks, offload to background workers or separate processes.

# FastAPI and Async — How They Relate

## FastAPI basics
- FastAPI is an ASGI framework designed to support both async and sync endpoints.  
- Endpoints declared with async def run as coroutines on the event loop.  
- Endpoints declared with def run in a threadpool so they do not block the event loop.

## ASGI vs WSGI
- WSGI is synchronous; frameworks like Flask traditionally use WSGI.  
- ASGI supports async I/O and long-lived connections (websockets, server-sent events).  
- FastAPI is ASGI-native and typically served with Uvicorn or Hypercorn.

## Example: sync vs async endpoints in FastAPI
```python
from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

# Synchronous endpoint (runs in a threadpool)
@app.get("/sync")
def sync_endpoint():
  time.sleep(2)  # blocking sleep: blocks the thread, not the whole process
  return {"message": "sync done"}

# Asynchronous endpoint (does not block event loop while awaiting)
@app.get("/async")
async def async_endpoint():
  await asyncio.sleep(2)  # non-blocking sleep: yields to event loop
  return {"message": "async done"}
```

Notes:
- FastAPI will run the sync endpoint in a worker thread so the event loop isn't blocked, but threads are limited — heavy blocking can exhaust threadpool capacity.
- Prefer async when you can use non-blocking libraries (async DB client, async HTTP client).

## Blocking calls in async handlers
- Use run_in_threadpool or asyncio.to_thread for CPU/blocking operations:
```python
from fastapi.concurrency import run_in_threadpool

@app.get("/blocking")
async def blocking():
  result = await run_in_threadpool(some_blocking_function)
  return {"result": result}
```

## Background tasks and long-running work
- Use FastAPI BackgroundTasks or external workers (Celery, RQ) for long-running or CPU-heavy jobs:
```python
from fastapi import BackgroundTasks

def send_email(data):
  # blocking or long-running task
  pass

@app.post("/submit")
async def submit(data: dict, background_tasks: BackgroundTasks):
  background_tasks.add_task(send_email, data)
  return {"status": "queued"}
```

# Clients: sync vs async libraries

- Sync HTTP client: requests
  ```python
  import requests
  response = requests.get("https://api.example.com")
  ```
- Async HTTP client: httpx (async) or aiohttp
  ```python
  import asyncio
  from httpx import AsyncClient

  async def fetch():
    async with AsyncClient() as client:
      r = await client.get("https://api.example.com")
      return r.text

  asyncio.run(fetch())
  ```

# Databases and I/O libraries
- Use async drivers for async endpoints (e.g., asyncpg for Postgres, databases, async versions of SQLAlchemy).  
- If only sync drivers exist, call them in a threadpool or keep endpoints sync.  
- ORMs: sqlalchemy has async support (1.4+), Tortoise ORM, or use micro ORMs or direct async drivers.

# Relation to HTTP/HTTPS, Proxies, and Infrastructure
- Async servers (ASGI) handle large numbers of concurrent connections efficiently — useful for APIs served over HTTPS.  
- Reverse proxies, load balancers, and CDNs remain important for scaling, SSL termination, and routing regardless of sync vs async.  
- When using SSL/TLS (HTTPS), perform TLS termination at the edge (load balancer, reverse proxy) or at the app server if required — either approach works with sync or async apps.

# When to choose what
- Small apps, simple workloads, or when using blocking libraries: sync endpoints are fine.  
- High-concurrency, I/O-bound APIs (many simultaneous requests, websockets, streaming): prefer async with FastAPI and async libraries.  
- For mixed environments, FastAPI supports both; convert heavy blocking work to background tasks or threadpool.

# Additional Components in Client-Server and HTTP/HTTPS Architecture

## 1. Proxy Server
- **Proxy server** acts as an intermediary between clients and servers.  
- Can cache responses, filter requests, and provide anonymity.  
- Useful for load balancing and security.

## 2. Load Balancer
- **Load balancer** distributes incoming client requests across multiple servers.  
- Improves reliability and scalability.  
- Can be hardware or software-based.

## 3. Firewall
- **Firewall** monitors and controls incoming and outgoing network traffic.  
- Protects servers from unauthorized access and attacks.  
- Can be network-based or host-based.

## 4. Reverse Proxy
- **Reverse proxy** receives client requests and forwards them to backend servers.  
- Can handle SSL termination, caching, and compression.  
- Often used to hide internal server details.

## 5. API Gateway
- **API gateway** manages API requests, authentication, rate limiting, and routing.  
- Centralizes API management and security.  
- Common in microservices architectures.

## 6. Database Server
- **Database server** stores and manages application data.  
- Responds to queries from the server application.  
- Examples: MySQL, PostgreSQL, MongoDB.

## 7. CDN (Content Delivery Network)
- **CDN** distributes content across geographically dispersed servers.  
- Reduces latency and improves load times for clients.  
- Commonly used for static assets like images and scripts.

## 8. Authentication Server
- **Authentication server** verifies user identities and issues tokens or credentials.  
- Supports protocols like OAuth, OpenID Connect, and SAML.  
- Essential for secure access control.

## 9. DNS Server
- **DNS server** translates human-readable domain names to IP addresses.  
- Enables clients to locate servers on the internet.  
- Critical for web and API accessibility.

## 10. Caching Layer
- **Caching layer** stores frequently accessed data to reduce server load and response time.  
- Can be implemented at client, proxy, or server level.  
- Examples: Redis, Memcached.

# Final summary
- Understand whether your workload is I/O-bound or CPU-bound.  
- FastAPI supports both sync and async endpoints — choose based on libraries and concurrency needs.  
- Use async for high-concurrency I/O workloads with compatible drivers; otherwise prefer sync or use threadpools/background workers to avoid blocking the event loop.  
- Combine HTTPS, reverse proxies, load balancers, and CDN to secure and scale your deployment.
