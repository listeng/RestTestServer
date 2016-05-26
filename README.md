# RestTestServer

## Usage

You can use this server for api test when writing a webapp. Once webapp request to server, the server will search the file which matched for the URL and return this text of file.

For example:

GET /api/users

server will return the content of file from ./api/getUsersList.txt

GET /api/users/12

server will return the content of file from ./api/getUsersById.txt