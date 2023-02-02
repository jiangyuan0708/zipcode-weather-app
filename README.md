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


now your docker should looks like: 


