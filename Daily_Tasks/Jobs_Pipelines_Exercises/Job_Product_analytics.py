# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.70.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


Product_Analytics = Job.from_dict(
    {
        "name": "Product Analytics",
        "trigger": {
            "pause_status": "UNPAUSED",
            "periodic": {
                "interval": 1,
                "unit": "HOURS",
            },
        },
        "tasks": [
            {
                "task_key": "Product_Analytics",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/azuser7222_mml.local@karthikirisoutlook.onmicrosoft.com/product_loader",
                    "source": "WORKSPACE",
                },
            },
        ],
        "queue": {
            "enabled": True,
        },
        "performance_target": "PERFORMANCE_OPTIMIZED",
    }
)

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.jobs.reset(new_settings=Product_Analytics, job_id=351909496240287)
# or create a new job using: w.jobs.create(**Product_Analytics.as_shallow_dict())
