import boto3

rds=boto3.client("rds","ap-southeast-2")

response=rds.create_db_instance_read_replica(
    SourceDBInstanceIdentifier="<source instance arn, see web console>",
    DBInstanceIdentifier="<the name you want to give to the replica>",
    KmsKeyId="<kms arn or id in the target region, if souce is not encrypted, no need to supply this>",
    SourceRegion="<source db region>",
    DBInstanceClass="db.<instance class>"
)

