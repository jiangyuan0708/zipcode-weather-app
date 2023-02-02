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

