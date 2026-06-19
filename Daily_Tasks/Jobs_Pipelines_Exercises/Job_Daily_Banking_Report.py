# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.70.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


Daily_Banking_Report = Job.from_dict(
    {
        "name": "Daily Banking Report",
        "trigger": {
            "pause_status": "UNPAUSED",
            "periodic": {
                "interval": 1,
                "unit": "DAYS",
            },
        },
        "tasks": [
            {
                "task_key": "Banking_Run",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/azuser7222_mml.local@karthikirisoutlook.onmicrosoft.com/bank_report",
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
w.jobs.reset(new_settings=Daily_Banking_Report, job_id=661857554738815)
# or create a new job using: w.jobs.create(**Daily_Banking_Report.as_shallow_dict())
