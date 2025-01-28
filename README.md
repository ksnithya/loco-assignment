# loco-assignment
Clone the repo,
git clone https://github.com/ksnithya/EKS-Terraform.git

To setup the scaling policy we need to install metric server in cluster so that it will collect the resources cpu and memory usage.
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

Also we need to add below entry in metric server deployment file to avoid certificate issue.

kubectl edit deployment metrics-server -n kube-system

args:
- --kubelet-insecure-tls
- --kubelet-preferred-address-types=InternalIP

