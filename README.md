# ECM2429-api

## Application Programming Interfaces (APIs)

The term API is now widely used in programming, although The meaning has changed over time, and can be quite vague - often just *the interface between one software system and another*.

APIs are typically documented with a description of how to make calls, and the format of the resulting data.

Today many APIs are programming language independent and use network connections. Such APIs are sometimes called Web APIs.

For the purpose of this module (Systems Development 2) we will consider the term API can be applied to both software libraries and Web APIs.

## Web APIs

A Web API is an API where the interface is one or more URIs (or URLs), that refer to services 
provided by a web server.

### Client-server overview

<https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview>

## HTTP and URIs

```
URI = scheme:[//authority]path[?query][#fragment]
```

The term URLs is generally used where the scheme (network protocol) is HTTP or HTTPS in which case the ```authority``` is a network ```host``` and ```port``` (80 and 443 are the defaults).

HTTP protocol consists of request and response messages. All modern programming languages have libraries that simplify the use of HTTP.  In Python we typically use the ```requests``` library.

In most cases Web APIs are *stateless*, which means that the service providing the API does not maintain states, or a session, from one call to the next.  Such services are called RESTful, where REST is an acronym of **Representational state transfer**.

## RESTful service operations and HTTP verbs

Remember these using acronym *CRUD*.

**Create** Implemented using HTTP POST, which creates the resource with the given URI.

**Read**  Implemented using HTTP GET, which reads the resource and returns its value.

**Update**  Implemented using HTTP PUT, which modifies an existing resource.

**Delete**  Implemented using HTTP DELETE, which makes the resource inaccessible using the specified URI.

## HTTP headers

### Authentication

### Content type

### Others

* Language

## JSON and XML

## The eBay APIs

For the assignment you are required to use data from an online shopping service.

## References

Sommerville, I. 2019. . Engineering Software Products. Pearson.

