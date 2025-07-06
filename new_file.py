import boto3

def create_s3_bucket(bucket_name, region):
    s3_client = boto3.client('s3', region_name=region)
    try:
        if region == 'us-east-1':
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"S3 bucket '{bucket_name}' created successfully.")
    except s3_client.exceptions.BucketAlreadyOwnedByYou:
        print(f"S3 bucket '{bucket_name}' already exists and is owned by you.")
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")

def create_sagemaker_notebook(notebook_name, role_arn, s3_bucket, region):
    sm_client = boto3.client('sagemaker', region_name=region)
    try:
        response = sm_client.create_notebook_instance(
            NotebookInstanceName=notebook_name,
            InstanceType='ml.t2.medium',
            RoleArn=role_arn,
            DefaultCodeRepository='',
            DirectInternetAccess='Enabled',
            VolumeSizeInGB=5,
            DefaultS3Bucket=s3_bucket
        )
        print(f"SageMaker notebook '{notebook_name}' created successfully.")
    except sm_client.exceptions.ResourceLimitExceeded:
        print(f"Limit exceeded for notebook instances.")
    except sm_client.exceptions.ResourceInUse:
        print(f"Notebook '{notebook_name}' already exists.")
    except Exception as e:
        print(f"Error creating SageMaker notebook: {e}")

def main():
    region = 'us-east-1'  # Change as needed
    name = 'ankit'        # Replace with your desired name
    role_arn = 'arn:aws:iam::123456789012:role/SageMakerExecutionRole'  # Update with your SageMaker role

    base_name = f"il-it-{name}-nprod"
    bucket_name = base_name.lower()
    notebook_name = base_name

    create_s3_bucket(bucket_name, region)
    create_sagemaker_notebook(notebook_name, role_arn, bucket_name, region)

if __name__ == "__main__":
    main()
