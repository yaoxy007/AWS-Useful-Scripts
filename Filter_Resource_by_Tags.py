import boto3

tags=boto3.client("resourcegroupstaggingapi","ap-southeast-2")

resource = tags.get_resoures(TagFilters=[{'Key':'<tag key>','Values':['<tag values>',]},])