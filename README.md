# Docker Mircroservices Integration

Please follw the instructions to have the app run on your local machine.

## Guidance and Result

Install the docker:
https://docs.docker.com/get-started/overview/

clone the repository

```
https://github.com/jiangyuan0708/zipcode-weather-app.git
```

builder the docer image for two services

cd into zipcode_service folder, then run
```
docker build -t zipcode-service .
```

cd into weateher_service folder, then run
```
docker build -t weather-service .
```

now you will have two image created and let's run them

run the zipcode service: 
```
docker run -dp 3000:3000 zipcode-service
```

run the weather service: 
```
docker run -dp 3001:3001 weather-service
```

now your docker should looks like: 

<img width="1015" alt="image" src="https://user-images.githubusercontent.com/124235505/216268363-2cc599e1-ecad-4e4d-9562-193b4563d13f.png">

We can see that zipcode service is running on 3000 port:
![image](https://user-images.githubusercontent.com/124235505/216268724-45f14b7e-cdf0-4dac-8320-30f5fe0f54e9.png)
![image](https://user-images.githubusercontent.com/124235505/216269029-6c671077-19f4-4a9c-be1a-c65028b274df.png)

We can see that weather service is running on 3001 port:
![image](https://user-images.githubusercontent.com/124235505/216268861-d56ba1f1-8d5e-43ca-8204-bab3cff3480d.png)
![image](https://user-images.githubusercontent.com/124235505/216268931-fd03c321-0097-4ef3-af9d-8ae525f82925.png)

Now if you want to integrate those two service, please run the client.py:
```
python client.py
```

the result looks like:
![image](https://user-images.githubusercontent.com/124235505/216269245-3b80f874-ec2a-46ba-99f8-bb9e18b16641.png)
