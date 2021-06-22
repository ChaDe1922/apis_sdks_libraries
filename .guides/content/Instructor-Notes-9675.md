##
This is a teacher/TA only page that gives instructors guidance on their teacher-led 30-45 minutes. This page is followed by the student-driven activity that will be completed after the more teacher-led time slot.

Instructors can create slides, examples, or other visual aids to help bring the concepts to life.

## Learning Objectives
Students Will Be Able To...
1. Explain how libraries, SDKs, APIs, and frameworks are different, yet related
1. Describe how an API works using the correct terminology
1. Implement authentication for an API in python
1. Implement a POST request for an API in python

## Outline of what to cover and suggested interactions
**1.0 What are Libraries, SDKS, Frameworks and APIs?**
   * Have students throw their guesses into chat before you answer this
   
   * You've already used libraries with python! A library is a rather narrowly scoped set of re-usable code. Examples - csv, time, pandas, matplotlib
   * An SDK is a set of libraries. Examples - Android has an SDK or set of libraries for developing an Android app.
   * A framework has many libraries (and/or SDKs) and APIs.
   * An API is a special king of library that accesses data.
   
**2.0 APIs**
* API stands for Application Programming Interface.
* APIs are sets of rules that allow interaction between applications.
* Similar to libraries, APIs let you add functionality without programming it from scratch

2.1 When are APIs used?
 * Open or Public APIs
 * Partner APIs - for interfacing between products
 * Internal or Private APIs
 
2.2 Types of APIs
 * REST - most popular type - 6 guiding principles (https://restfulapi.net/)
 * SOAP - similar to REST but less popular due to strict security requirements
 * RPC (XML and JSON)

2.3 How do APIs work?
Provide an overview, making sure to cover the following terms:

* Client
* Server
* Resource
* Parameters

* HTTP Request Methods - https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods
    * GET request
    * POST request
* Response
    * Head
    * Body
* Rate Limit - number of requests you can make

* Authentication
    * oAuth
    
**3.0 Reading API docs**
Model how you would read the Spotify API docs: https://developer.spotify.com/documentation/web-api/

Explicitly call out connections to vocabulary and note anything that effects implementation.

3.1 Libraries
Sometimes, APIs have language specific libraries to make them even easier to use: https://spotipy.readthedocs.io/en/2.18.0/

**4.0 Simple API project**
Put together a simple API project (example: https://github.com/mgric/Spotify-Python-Projects). See Live Coding teaching tip below.

Note: Students are going to learn how to parse JSON in the next lesson so try to model POST requests as opposed to GET requests.

**5.0 Closing**

5.1 Questions?

5.2 Give a sentence overview of the activity they are about to do

5.3 Explain how to get help from Instructors and TAs


## Teaching Tips

### Live Coding
Don't just show learners an already built system -- start from absolute scratch like they'll be doing and MAKE MISTAKES! Normalize making the mistake -- everyone does it. Normalize asking for help -- everyone should do it. Model how to listen to someone's suggestion and try it out -- they will be doing paired programming and need to see good examples of how navigators can support drivers.
