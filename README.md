# Birthdays

Birthdays is a Python app that automates sending birthday emails. It can be made to run every day through GitHub actions and cron scheduling and gets its data from a secured external source like a REST API endpoint.

## Download

To set up app locally first download the app to your local machine. This can be done through various means.

### Download The Repository

You can either download the whole repository by running the following command on your terminal.

```bash
git clone git@github.com:Thavarshan/birthdays.git
```

### Download The Source Code

You can also download the app by clicking [here](https://github.com/Thavarshan/birthdays/archive/refs/tags/v2.0.2.zip).

## Installation

To install the application and it's dependencies, navigate into the application directory and run the followinf commands within the application directory.

First setup and activate Python virtual environment.

```bash
python3 -m venv ./venv && source ./venv/bin/activate
```

Then install all application dependencies by running:

```bash
pip install -r requirements.txt
```

That should get the app installed and ready to use.

### Usage

Before starting up the app make sure you have the proper credentials.

You can store sensitive data within the environment file provided in the application. You may find an `.env.example` file within the application directory which you can use to store these credentials. Just rename it to a valid environment file name like below.

```bash
cp .env.example .env
```

Now you are ready to run the application. Simple run:

```bash
python3 app.py
```

## Basic Features

- Can be made to run every day at 05:45 GMT,
- Send a GET request to an external API where the data lives.
- Receives a JSON response from external server (content: people details)
- Iterates through each person detail, specifically their birthdays
- Converts `ISO` standard time format to string format of "day-month" `d-m` and matches with the date the app is running (present date)
- If a match was found
    - Gets person name and email
    - Picks out a random poem from `JSON` file source located within the app
    - Builds an email message with name and content
    - sends an email to said person through SMTP or SendGrid
- If no match was found continues with the iteration until one is found or finished its run

## External API

PHP cloud-based app hosted on a cloud server with bank-grade security levels. A data breach is nearly impossible. Contact details are saved within a `PostgreSQL` database within the hosting platform and cannot be altered by any means except through my account on the host.

An example response that is acceptable by the application is given below. Make sure any response received by an external source follows the same format.

##### Example Response Body


```json
[
    {
        "id": 1,
        "name": "John Benson",
        "phone": "0770000011",
        "company": "Nord Group, Inc",
        "slug": "john-benson",
        "email": "johnson.ben@example.com",
        "birthday": "1994-02-25",
        "profile_photo_path": null,
        "created_at": "2021-06-19T04:33:32.000000Z",
        "updated_at": "2021-06-19T04:33:32.000000Z",
    }
]
```

### How a Secure Connection is Made Between the Python App and PHP Web App

- An API token must be generated from the console of the host within the PHP app. This can only be done through a secure terminal connection through my account on the hosting platform.
- The generated token is then saved within the secret environment variables on `GitHub` which cannot be accessed unless logged into my GitHub account.
- The Python app then makes a `GET` request with the generated token as the "Bearer token" for authorization of the PHP app.
- The PHP app then receives the request, authenticates its validity, and if successfully authenticated, serves the request with a query of all the student details as a `JSON` response. In the case, the authentication fails the PHP app sends the `401` not authorized response.

## Contributing

Thank you for considering contributing to Birthdays! You can read the contribution guide [here](.github/CONTRIBUTING.md).

## Security Vulnerabilities

Please review [our security policy](https://github.com/Thavarshan/birthdays/security/policy) on how to report security vulnerabilities.

## License

Birthdays is open-sourced software licensed under the [MIT license](LICENSE).
