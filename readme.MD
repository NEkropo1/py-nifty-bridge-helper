# Nifty Bridge GPT Helper

 - A powerful and RESTFUL API which helps you with Nifty Bridge info
 - Contains Redis VB as base for EMBEDDINGS
 - GPT 3.5-turbo as answer adviser
 - Blocks you from sending more than 4096 tokens
 - Post method protected via .env X_API_TOKEN
 - Very simple to use
 - Swagger/Redoc
 - Dockerized

# Installation:

```
git clone git@github.com:NEkropo1/py-nifty-bridge-helper.git
cd py-nifty-bridge-helper
```

Create a new .env file by copying .env.sample with  
`cp .env.sample .env` on Linux or simply copypaste on Windows.  

Open the .env file in a text editor and update the values of the environment variables  
according to sample.  

If you don't have Docker, install it via official guide:
# Ubuntu https://docs.docker.com/engine/install/ubuntu/
# Windows https://docs.docker.com/desktop/install/windows-install/

If you already have docker, simply use:
```
docker-compose up --build
```
Now you will have app running on your device

Some documentation:
 -localhost:8000/docs#/ - Swagger API documentation  
 -localhost:8000/redoc/ - Redoc API documentation  

Or use anything you need to work with endpoints.
Some screenshots:
![image](https://github.com/NEkropo1/py-nifty-bridge-helper/assets/107141441/c7bf537f-6f19-4e9e-966d-9c7709b6dc58)
![image](https://github.com/NEkropo1/py-nifty-bridge-helper/assets/107141441/c320fb04-67a4-4432-9647-3dcece73d580)
![image](https://github.com/NEkropo1/py-nifty-bridge-helper/assets/107141441/f3e5c074-b13e-4a86-98b6-b077ff11ff77)
![image](https://github.com/NEkropo1/py-nifty-bridge-helper/assets/107141441/bc8d713c-7d31-4446-93cc-e7c51f5ddd62)
