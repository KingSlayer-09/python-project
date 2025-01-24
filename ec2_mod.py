import boto3

def create_ec2_instances(
    key_name,
    security_group,
    instance_type="t2.micro",
    image_id="ami-0abcdef1234567890",
    min_count=1,
    max_count=1,
    region_name="us-east-1"
):
    """
    Launch multiple EC2 instances.

    :param key_name: Name of the key pair.
    :param security_group: Name or ID of the security group.
    :param instance_type: EC2 instance type (default: t2.micro).
    :param image_id: AMI ID (default: ami-0abcdef1234567890).
    :param min_count: Minimum number of instances to launch.
    :param max_count: Maximum number of instances to launch.
    :param region_name: AWS region where the instances will be created.
    """
    ec2_client = boto3.client("ec2", region_name=region_name)

    try:
        response = ec2_client.run_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroups=[security_group],
            MinCount=min_count,
            MaxCount=max_count,
        )

        instance_ids = [instance["InstanceId"] for instance in response["Instances"]]
        print(f"Successfully launched instances: {instance_ids}")
        return instance_ids

    except Exception as e:
        print(f"Error launching instances: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace the following values with your specific details
    KEY_NAME = "your-key-name"
    SECURITY_GROUP = "your-security-group"
    INSTANCE_TYPE = "t2.micro"
    IMAGE_ID = "ami-0abcdef1234567890"  # Replace with a valid AMI ID for your region
    MIN_COUNT = 2  # Minimum number of instances
    MAX_COUNT = 3  # Maximum number of instances
    REGION = "us-east-1"  # AWS region

    create_ec2_instances(
        key_name=KEY_NAME,
        security_group=SECURITY_GROUP,
        instance_type=INSTANCE_TYPE,
        image_id=IMAGE_ID,
        min_count=MIN_COUNT,
        max_count=MAX_COUNT,
        region_name=REGION
    )
