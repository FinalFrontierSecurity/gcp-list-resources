## List GCP Resources
Install gcloud and authenticate via `gcloud init`

Run the following command:

```gcloud asset list --project <PROJECT NAME> --format="csv(ancestors[0].split('/').slice(-1):sort=1:label=Project,name.split('/').slice(-3):label=Region:sort=2,assetType,name.split('/').slice(-1))" > gcp_inventory.csv```