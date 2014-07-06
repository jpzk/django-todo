# Django-Todo

This project is part of this [tutorial](http://www.madewithtea.com/simple-todo-api-with-django-and-oauth2.html) how to implement a simple Todo REST API with Django, Django REST Framework and OAuth2.

## Example 

### Register a User

<pre>
curl -X POST -d 'username=jpzk&password=yourguess'\
http://localhost:8000/register/
</pre>

### Get Authentication Token

<pre>
curl -X POST -d
'username=jpzk&password=yourguess&grant_type=password&client_id=jpzk'
http://localhost:8000/oauth2/access_token/
 
{"access_token": "41b59e8238bb418c1fc98cfc6f523dd1a7839a03", "token_type":
"Bearer", "expires_in": 2591999, "scope": "read"} 
</pre>

### Create a Todo

<pre>
curl -X POST -H 'Content-Type: application/json' -H 'Authorization: bearer
41b59e8238bb418c1fc98cfc6f523dd1a7839a03' -d '{"description":"bake a bread"}'
http://localhost:8000/todos/ 
</pre>

### Get All Todos

<pre>

</pre>

### Update a Todo

<pre>
curl -X PUT -H 'Content-Type: application/json' -H 'Authorization: bearer
00db9a38ea3f86d04dd3eeded9128620f11158eb' -d '{"description":"bake a bread",
"done":"True"}' http://localhost:8000/todos/1
</pre> 
