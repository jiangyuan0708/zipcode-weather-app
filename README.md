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

cd into weateher_service folder, then run
```
docker build -t weather-service .
```

then run the weather-service:
```
docker run -dp 3001:3001 weather-service
```
Now we weather-service deployed.
To make two containers communicate with each other, let's use the default bridge network as they are in the same host.
Now since we need zipcode service to call weather service, let's fetch the IP address of the zipcode container:

copy the id of weather-service:
<img width="978" alt="image" src="https://user-images.githubusercontent.com/124235505/217765014-38576307-275f-47d7-b5a5-db72d62a91d8.png">

then run:
```
docker inspect 134a4351f800c45badf317c0206229808acc8910ef01fd5d47301fa599795d2c | grep IPAddress
```

![image](https://user-images.githubusercontent.com/124235505/217764635-71fcd04e-5f8d-49da-8efe-e86bd5a6a7f6.png)

Now we paste the ip address to the app.py in zipcode service
```
response = requests.get(f"http://172.17.0.2:3001/weather/{zip}")
```

Now we can deploy the zipcode service:

cd into zipcode_service folder, then run
```
docker build -t zipcode-service .
```

run the zipcode service: 
```
docker run -dp 3000:3000 zipcode-service
```

now your docker should looks like: 

<img width="1015" alt="image" src="https://user-images.githubusercontent.com/124235505/216268363-2cc599e1-ecad-4e4d-9562-193b4563d13f.png">

We can see that zipcode service is running on 3000 port:

successful:

![image](https://user-images.githubusercontent.com/124235505/216268724-45f14b7e-cdf0-4dac-8320-30f5fe0f54e9.png)

Not found:

![image](https://user-images.githubusercontent.com/124235505/216269029-6c671077-19f4-4a9c-be1a-c65028b274df.png)

We can see that weather service is running on 3001 port:

successful:

![image](https://user-images.githubusercontent.com/124235505/216268861-d56ba1f1-8d5e-43ca-8204-bab3cff3480d.png)

Not found:

![image](https://user-images.githubusercontent.com/124235505/216268931-fd03c321-0097-4ef3-af9d-8ae525f82925.png)


Now please run the client.py:
```
python client.py
```
it will call zipcode service, then zipcode service call weather service, and return the result
the result looks like:
![image](https://user-images.githubusercontent.com/124235505/217765771-48d3bebb-9ab6-4fd4-9264-2631622d0b39.png)
