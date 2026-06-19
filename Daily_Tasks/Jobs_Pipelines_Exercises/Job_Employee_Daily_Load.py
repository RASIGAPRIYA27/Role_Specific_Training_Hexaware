# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.70.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


Employee_Daily_Load = Job.from_dict(
    {
        "name": "Employee Daily Load",
        "trigger": {
            "pause_status": "UNPAUSED",
            "periodic": {
                "interval": 1,
                "unit": "DAYS",
            },
        },
        "tasks": [
            {
                "task_key": "Employee_Daily_Load",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/azuser7222_mml.local@karthikirisoutlook.onmicrosoft.com/employee_loader",
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
w.jobs.reset(new_settings=Employee_Daily_Load, job_id=497060153365630)
# or create a new job using: w.jobs.create(**Employee_Daily_Load.as_shallow_dict())


