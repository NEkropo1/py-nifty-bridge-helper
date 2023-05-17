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
![image](https://github.com/NEkropo1/py-nifty-bridge-helper/assets/107141441/f60af22f-e13f-40db-8611-06e4827be75f)
![image](https://github.com/NEkropo1/py-nifty-bridge-helper/assets/107141441/17720e48-cede-4278-bcdf-8eb5ca4281e6)
![image](https://github.com/NEkropo1/py-nifty-bridge-helper/assets/107141441/42c788cc-8ba1-4182-8dde-312cd84643ec)
![image](https://github.com/NEkropo1/py-nifty-bridge-helper/assets/107141441/cde9cd18-b5c1-43d0-a65b-6f2f3091e337)
![image](https://github.com/NEkropo1/py-nifty-bridge-helper/assets/107141441/d3dad2b0-d430-4416-96ff-f9847bca252f)
