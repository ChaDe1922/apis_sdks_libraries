##

Before trying a complex example, let's start with a sentiment analysis API which returns sentiment analysis information when you send it text.

Here is the documentation: http://text-processing.com/docs/sentiment.html

1. Import `requests`

1. Get text from the user to send to the API

1. Do a POST request. As a reminder, you can set it up like this:
     ```python
        url = 'http://text-processing.com/api/sentiment/'
        myobj = {'text': 'somevalue'}

        response = requests.post(url, data = myobj)
      ```
      
1. Print out the response (`response.json()`)

{Run code | terminal}(python3 sentiment.py)

{Check It!|assessment}(code-output-compare-3837208471)


|||guidance

## sample solution
```python
import requests

text = input("Enter text to analyze: ")

url = 'http://text-processing.com/api/sentiment/'
myobj = {'text': text}
response = requests.post(url, data = myobj)

print(response.json())
```

|||