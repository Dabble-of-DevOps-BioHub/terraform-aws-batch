DATA_S3 = "bioanalyze-ec2-test-nf-rnaseq-06o3qdtm7v"
JOB_S3 = DATA_S3


# These come from the terraform code in auto-deployment/terraform
ECR = "dabbleofdevops/nextflow-rnaseq-tutorial"
COMPUTE_ENVIRONMENT = "bioanalyze-ec2-test-nf-rnaseq"
JOB_DEF_NAME = "bioanalyze-ec2-test-nf-rnaseq"
JOB_QUEUE_NAME = "bioanalyze-ec2-test-nf-rnaseq-default-job-queue"
JOB_ROLE = "arn:aws:iam::018835827632:role/bioanalyze-ec2-test-nf-rnaseq-batch_execution_role"
SECRET_NAME = "bioanalyze-ec2-test-nf-rnaseq"
SECRET_ARN = "arn:aws:secretsmanager:us-east-1:018835827632:secret:bioanalyze-ec2-test-nf-rnaseq-Zg7kMY"