# Mock API Helper - Helps development teams in mocking API responses.
### 🗂️ Integrated with Redis cache and API rate limiter.

## Usage after setup:

#### 1. Access the project at http://127.0.0.1:8000/

<img width="826" height="521" alt="img1" src="https://github.com/user-attachments/assets/0c77d8fe-0b8b-40a7-9675-81f98b75b652" />

#### 2. Click Add or Update project for adding new projects or updating existing ones.

<img width="826" height="413" alt="img2" src="https://github.com/user-attachments/assets/1a16ce70-385d-4cb3-8ed0-6f91f55229c0" />

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

<br>
<p align="center">
  Like it? ❤️ <a href="https://linkedin.com/in/aashish-malviya">Let's connect 🤗</a>
</p>
