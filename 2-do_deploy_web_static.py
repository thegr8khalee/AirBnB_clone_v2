#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env, put, run
from fabric.context_managers import cd

# Define remote hosts
env.hosts = ["54.160.85.72", "35.175.132.106"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        return False

    # Extract file name and name without extension
    file_name = os.path.basename(archive_path)
    name = os.path.splitext(file_name)[0]

    # Remote directory paths
    remote_tmp_dir = "/tmp/"
    remote_release_dir = "/data/web_static/releases/{}/".format(name)
    remote_current_dir = "/data/web_static/current"

    # Transfer the archive to the remote server's /tmp directory
    put(archive_path, remote_tmp_dir)

    # Create release directory
    run("mkdir -p {}".format(remote_release_dir))

    # Extract archive to release directory
    with cd(remote_release_dir):
        run("tar -xzf {} -C .".format(os.path.join(remote_tmp_dir, file_name)))

    # Delete temporary archive file
    run("rm {}".format(os.path.join(remote_tmp_dir, file_name)))

    # Move contents from web_static directory to release directory
    run("mv {}web_static/* {}".format(remote_release_dir, remote_release_dir))

    # Remove now-empty web_static directory
    run("rm -rf {}web_static".format(remote_release_dir))

    # Update symbolic link
    run("rm -rf {}".format(remote_current_dir))
    run("ln -s {} {}".format(remote_release_dir, remote_current_dir))

    return True
