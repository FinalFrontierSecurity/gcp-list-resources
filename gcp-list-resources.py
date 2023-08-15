import subprocess


subprocess.Popen(['gcloud','init'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
process = subprocess.Popen(['gcloud','asset','list','--project {0}'.format(project)], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
gcloud init
gcloud asset list --project grounded-region-396000 --format="csv[]"
