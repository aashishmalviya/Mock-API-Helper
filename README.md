# Mock API Helper

## Usage after setup:

#### 1. Access the project at http://127.0.0.1:8000/

![image](https://github.com/user-attachments/assets/99231b7e-2f99-4bc5-abc1-3fb502ef75d8)

#### 2. Click Add or Update project for adding new projects or updating existing ones.

![image](https://github.com/user-attachments/assets/7cdd4400-5a82-4ff4-a251-effc0995fdcb)

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
