# kubernetes hello world

This repo demonstrates a basic Kubernetes setup. 

Follow along in the detailed self-guided walk-through here: https://www.linkedin.com/pulse/containerized-apps-part-3-up-running-kubernetes-samuel-edeh/

Clone the repo:

```shell script
git clone https://github.com/sedeh/kubernetes-hello.git
```

Create a local docker registry, build the container images, tag, and push them:
 
```shell script
docker run -d -p 5000:5000 --restart=always --name local registry:2
cd app1
docker build --tag app1:1.0 .
docker tag app1:1.0 localhost:5000/app1:1.0
docker push localhost:5000/app1:1.0
cd ../app2
docker build --tag app2:1.0 .
docker tag app2:1.0 localhost:5000/app2:1.0
docker push localhost:5000/app2:1.0
cd ../main
docker build --tag main:1.0 .
docker tag main:1.0 localhost:5000/main:1.0
docker push localhost:5000/main:1.0
cd ..
```

Run the multi-container app:

```shell script
kubectl create namespace hello
kubectl config set-context --current --namespace=hello
kubectl apply -f docker-compose-k.yml
kubectl get deploy
```

To see the actual containers or pods, execute:

```shell script
kubectl get pod
```

Copy one of the pods and stream the log. Something like: 

```shell script
kubectl logs -f main-deployment-7947f5df57-pdfbc
```

Test the app:

```shell script
curl http://0.0.0.0:30000/
```

If successful, you will see an output like:

```json
{"app1-deployment-6fd7554c44-zptdf": "hello from app1",
 "app2-deployment-5f9986ccff-xf6vm": "hello from app2",
 "main-deployment-7947f5df57-pdfbc": "hello from main"}
```

Essentially, main is listening on port 30000 on the host machine and communicates with app1 and app2 on port 8080.

The output shows we were able to reference a custom and a native environment variables.

Tear down the app:

```shell script
kubectl delete namespace hello
```