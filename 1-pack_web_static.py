#!/usr/bin/python3
# Fabfile to generate a .tgz archive from the contents of web_static.
import os
import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    # Create a directory if it doesn't exist to store versions
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Get current timestamp for the archive name
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")

    # Name of the archive file
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    # Create the .tgz archive
    result = local("tar -czvf {} web_static".format(archive_name))

    # Check if the command executed successfully
    if result.failed:
        return None

    return archive_name
