module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "19.21.0"

  cluster_name    = "day6-eks"
  cluster_version = "1.29"
  subnet_ids      = ["subnet-0068cda7254a82a7e", "subnet-01584c46c734a3860"] # replace with your subnet IDs
  vpc_id          = "vpc-0e8710c971fcc64f5"                     # replace with your VPC ID

  eks_managed_node_groups = {
    default = {
      min_size     = 1
      max_size     = 2
      desired_size = 1
      instance_types = ["t3.medium"]
    }
  }
}



