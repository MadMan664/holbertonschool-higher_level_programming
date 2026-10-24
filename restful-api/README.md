# RESTful API

Tasks 0 and 1 are explained below. Tasks 2 to 5 are scripts.

Install the requirements with:


    pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended


## Task 0. Basics of HTTP/HTTPS

### HTTP versus HTTPS

| | HTTP | HTTPS |
|---|------|-------|
| Port | 80 | 443 |
| Encryption | None, the data travels as plain text | SSL/TLS encrypts the data |
| Who can read it | Anyone on the path (Wi-Fi, router, provider) | Only the client and the server |
| Tampering | Possible without being noticed | Detected, the data is signed |
| Identity of the server | Not checked | Checked with a certificate |
| Typical use | Public pages with nothing private | Banking, e-mail, logins, any API |

### Structure of a request and a response


    Request                                   Response
    -------                                   --------
    GET /posts HTTP/1.1                       HTTP/1.1 200 OK
    Host: jsonplaceholder.typicode.com        Content-Type: application/json
    Accept: application/json                  Content-Length: 27520

    (empty body for a GET)                    [ {"userId": 1, "id": 1, ...}, ... ]


- First line of a request: method, path, protocol version.
- First line of a response: protocol version, status code, reason.
- Then the headers (`Name: value`), an empty line, and the optional body.

### Common methods

| Method | Description | Use case |
|--------|-------------|----------|
| GET | Retrieves data | Fetching a web page or the list of posts of an API |
| POST | Sends data to create a resource | Submitting a form, creating a user |
| PUT | Replaces a resource | Updating all the fields of a user |
| PATCH | Changes part of a resource | Updating only the e-mail of a user |
| DELETE | Removes a resource | Deleting a post |

### Common status codes

| Code | Description | Scenario |
|------|-------------|----------|
| 200 | OK | A GET request that worked |
| 201 | Created | A POST that created a new user |
| 301 | Moved Permanently | A page that now lives at another URL |
| 400 | Bad Request | The JSON sent to the API is invalid |
| 401 | Unauthorized | A protected route called without valid credentials |
| 403 | Forbidden | A logged in user calls a route reserved to admins |
| 404 | Not Found | A requested page or resource does not exist |
| 500 | Internal Server Error | The server crashed while handling the request |

Groups: 1xx informational, 2xx success, 3xx redirection, 4xx client error,
5xx server error.

## Task 1. curl


    curl --version
    curl http://example.com
    curl https://jsonplaceholder.typicode.com/posts
    curl -I https://jsonplaceholder.typicode.com/posts
    curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts


- `--version` shows the installed version and the supported protocols.
- The `posts` request returns a JSON array of posts (`userId`, `id`,
  `title`, `body`).
- `-I` sends a HEAD request and prints only the status line and the headers.
- `-X POST -d` sends the data with a POST; JSONPlaceholder answers with the
  created post and `"id": 101`. Nothing is really saved.
- Pipe the output to `jq` to read it more easily.

## Task 2. Requests

`task_02_requests.py`: `fetch_and_print_posts()` prints the status code and
the titles, `fetch_and_save_posts()` writes `id`, `title` and `body` to
`posts.csv`.

## Task 3. http.server

`task_03_http_server.py` listens on port 8000.

| Path | Answer |
|------|--------|
| `/` | `Hello, this is a simple API!` |
| `/data` | `{"name": "John", "age": 30, "city": "New York"}` |
| `/status` | `OK` |
| `/info` | `{"version": "1.0", "description": "A simple API built with http.server"}` |
| anything else | 404 `Endpoint not found` |

## Task 4. Flask

`task_04_flask.py`, run with `flask --app task_04_flask.py run`. The users
are kept in memory, the dictionary starts empty.

| Route | Answer |
|-------|--------|
| `/` | `Welcome to the Flask API!` |
| `/data` | list of usernames |
| `/status` | `OK` |
| `/users/<username>` | the user, or 404 `User not found` |
| `POST /add_user` | 201 `User added`; 400 `Invalid JSON`; 400 `Username is required`; 409 `Username already exists` |

## Task 5. Security

`task_05_basic_security.py` has Basic authentication, JWT, and a role check.
Every authentication error answers 401; a valid token without the admin role
answers 403.

| Route | Method | Protection |
|-------|--------|------------|
| `/basic-protected` | GET | Basic authentication |
| `/login` | POST | gives a JWT for valid credentials |
| `/jwt-protected` | GET | JWT |
| `/admin-only` | GET | JWT with the role `admin` |

Test users: `user1` (role user) and `admin1` (role admin), password
`password`. The secret key is read from `JWT_SECRET_KEY`.
