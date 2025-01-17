# Mock API Helper - Helps development teams in mocking API responses.
### 🗂️ Integrated with Redis cache and API rate limiter.

## Usage after setup:

#### 1. Access the project at http://127.0.0.1:8000/

![image](https://github.com/user-attachments/assets/58814824-ad57-4a55-a858-e15d54da9d47)


#### 2. Click Add or Update project for adding new projects or updating existing ones.

![image](https://github.com/user-attachments/assets/9c11f05f-06fe-43ae-8600-e9852076269b)


#### 3. Add your project details, click Submit.

#### 4. To get saved JSON response:

##### GET :

```
curl -X GET http://127.0.0.1:8000/project_name/resource_name/
```

##### POST :
Generate token using
```
curl -c cookie.txt http://127.0.0.1:8000/project_name/resource_name/
```

use curl command as below:
```
curl --cookie cookie.txt http://127.0.0.1:8000/project_name/resource_name/ -H "X-CSRFToken: CSRF_TOKEN" -X POST

example:
curl --cookie cookie.txt http://127.0.0.1:8000/project_name/resource_name/ -H "X-CSRFToken: someCsrFtokEnValUeabcd0123456789" -X POST
```
