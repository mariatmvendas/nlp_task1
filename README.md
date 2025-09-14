# Task 1 - Sentiment analysis

Construct a Docker/Podman container less than 200 MB with a REST-based Web service with a Python program running from port 8000 that scores Danish or English course evaluations for sentiment.
The system must not use external Web services.
The API should be with the interface `/v1/sentiment` as HTTP POST.
The input is a JSON dictionary with the field `text`.
The Web service should return the response as JSON with a dictionary with the field ``score'' that is a float or integer value between
$-5$ and 5 where $-3$ is a common bad score, $-5$ really bad, 0 neutral, 3 good, 5 very good.
The Web service should have Swagger documentation. 
Examples of three course evaluation texts are
```
Det var en god lærer.
It was a bad course
It was a very dry course and I did not learn much.
```

When the lines are submitted individually to the web service, the values of the score field in the responses should be $3, -3, -3$, respectively.

## Version 1
Uses the example given by the teacher and it is able to correctly classify the three sentences by adding the option "dry" in the if statement.

## Version 2
Uses the affin lexicon with the langdetect tool to detect the languange and then perform sentiment analysis. It is not able to correctly classify the last sentence although the word "dry" was added to the affin dictionary.
