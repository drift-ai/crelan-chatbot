# myCrelan Chatbot

Public FAQ page chatbot for Crelan


## Endpoint

https://3hajmbyubh.eu-west-1.awsapprunner.com/

## AWS App runner

https://eu-west-1.console.aws.amazon.com/apprunner/home?region=eu-west-1#/services/dashboard?service_arn=arn%3Aaws%3Aapprunner%3Aeu-west-1%3A077590795309%3Aservice%2Fmycrelan-chatbot%2Fdc90a92e6d2d44e59739ee63b7167dcd&active_tab=logs

## Docker

### build and push

```bash
aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 077590795309.dkr.ecr.eu-west-1.amazonaws.com
docker build -t mycrelan-chatbot .
docker tag mycrelan-chatbot:latest 077590795309.dkr.ecr.eu-west-1.amazonaws.com/mycrelan-chatbot:latest
docker push 077590795309.dkr.ecr.eu-west-1.amazonaws.com/mycrelan-chatbot:latest
```

### run

```bash
docker run mycrelan-chatbot
```

