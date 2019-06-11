# Example Todo application
A simple distrubuted application running across multiple Docker containers.

This application will integrate concept of continious integration, delivry and deployment.

# Application components
**Main:**
- Front: User interface to manipulate Todo
- API: API to manipulate Todo
- DB: Store Todo
 
**Additionnal:**
- Reverse proxy: handle SSL decryption and loadbalancing
- Vault: store secret for login and https certificate

# Getting started
Please refer to `README.md` file of each application componant

## Run via Docker-compose
create `todo_app_db_username.txt` and `todo_app_db_username.txt` file by using command `echo -n "<username or passworw>" > file.txt`

```bash
docker-compose -f docker-compose.yml -f example-todo-application-api/docker-compose.yml up
```