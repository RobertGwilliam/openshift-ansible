"""Check that a yum update would not run into conflicts with available packages."""
from openshift_checks import OpenShiftCheck


class PackageUpdate(OpenShiftCheck):
    """Check that a yum update would not run into conflicts with available packages."""

    name = "package_update"
    tags = ["preflight"]

    def run(self):
        args = {"packages": []}
        return self.execute_module_with_retries("check_yum_update", args)
