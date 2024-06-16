Connect to remote server: 
* Refer to video: https://youtu.be/IXSiYkP23zo?si=dLfR4NwoZRAzfwIs
* In the terminal, navigate to root folder, make sure the key exists `mlops_zoomcamp.pem`.
* In the root folder, run `ssh -i ~/.ssh/mlops_zoomcamp.pem ubuntu@3.15.43.192`. The id should be replaced by each time running the instance, the value of "Public IPv4 address".
* Download the conda environment `wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh`
* To leave the vm `exit`
* `scp -r -i ~/.ssh/mlops_zoomcamp.pem /Users/yihanzhou/PycharmProjects/mlops-zoomcamp/ ubuntu@3.15.43.192:~/mlops-zoomcamp
`