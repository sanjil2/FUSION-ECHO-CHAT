import objc
from AppKit import NSWorkspace
import subprocess


def get_installed_applications():
    cmd = 'mdfind "kMDItemKind==Application"'
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        print(f"Error: {error.decode('utf-8')}")
        return []

    applications = output.decode('utf-8').split('\n')
    return applications


def app_collection(arr):
    for i in range(len(arr)):
        arr[i] = ''.join(arr[i].split('/')[-1].split('.')[:-1])


def open_application(app_name):
    cmd = f'open -a "{app_name}"'
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        print(f"Error: {error.decode('utf-8')}")


def close_application(app_name):
    script = f'tell application "{app_name}" to quit'
    cmd = ['osascript', '-e', script]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        print(f"Error: {error.decode('utf-8')}")


def get_opened_applications():
    apps_opened = []

    workspace = NSWorkspace.sharedWorkspace()
    running_apps_info = workspace.runningApplications()

    for app_info in running_apps_info:
        if app_info.activationPolicy() == 0:
            app_name = app_info.localizedName()
            apps_opened.append(app_name)

    return apps_opened


# Call the function to get the list of opened applications
opened_apps = get_opened_applications()

installed_apps = get_installed_applications()
app_collection(installed_apps)

# print(opened_apps)