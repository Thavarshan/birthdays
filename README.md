# Birthdays
Birthdays is a Python app that automates sending birthday emails. It runs every day through GitHub actions and cron scheduling and gets its data from a secured external source.

## Basic workflow
Runs every day at 05:45 GMT,
- Send a GET request to an external API where the data lives.
- Receives a JSON response from external server (content: student details)
- Iterates through each student detail, specifically their birthdays
- Converts ISO standard time format to string format of "day-month" and matches with the date the app is running (present date)
- If a match was found
    - logs into common ICBT Batch 95 Google account via OAuth client (very secure)
    - Gets student name and email
    - Picks out a random poem from JSON file source located within the app
    - Builds an email message with name and content
    - sends an email to said student
- If no match was found continues with the iteration until one is found or finished its run

## Source code of the Python app
Open source, and can be seen by everyone, but no changes can be made unless permitted by me (because it lives in my account). This isn't a big deal because student details are not found within the app's source code.

## External API
PHP cloud-based app hosted on a cloud server with bank-grade security levels. A data breach is nearly impossible. Student details are saved within a PostgreSQL database within the hosting platform and cannot be altered by any means except through my account on the host.

## How the secure connection is made between the Python app and PHP web app
- An API token must be generated from the console of the host within the PHP app. This can only be done through a secure terminal connection through my account on the hosting platform.
- The generated token is then saved within the secret environment variables on GitHub which cannot be accessed unless logged into my GitHub account.
- The Python app then makes a GET request with the generated token as the "Bearer token" for authorization of the PHP app.
- The PHP app then receives the request, authenticates its validity, and if successfully authenticated, serves the request with a query of all the student details as a JSON response. In the case, the authentication fails the PHP app sends the 401 not authorized response.





