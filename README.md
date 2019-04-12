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
