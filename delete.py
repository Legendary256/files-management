import os
import shutil

forbidden_dir = ['Files',
'Blacklist',
'Discord',
'Downloads',
'History',
'Steam',
'FileGrabber',
'Cookies',
'Autofill',
'Autofills',
'browsers',
'CheCkeR']

forbidden_files = ['InstalledSoftware',
'ProcessList',
'Screensho',
'DomainDetects',
'domain detect',
'InstalledBrowsers',
'UserInformation',
'User Information',
'@XIII_FREE_LOGS',
'@XIII_GET_PRIVATE_ACCESS',
'ABOUT_XIII_CLOUD',
'XIII_USER_INFORMATION',
'System Info',
'information.txt',
'information.bak',
'Desktop.png',
'Desktop.jpg',
'Clipboard.txt']

def remove_forbidden_items(root_dir, forbidden_dirs, forbidden_files):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path) and item in forbidden_dirs:
            shutil.rmtree(item_path) # remove the directory
            print(f"Folder removed - {item_path}")
        elif os.path.isfile(item_path):
            if any(substring in item for substring in forbidden_files):
                os.remove(item_path) # remove the file
                print(f"File removed - {item_path}")
        else:
            remove_forbidden_items(item_path, forbidden_dirs, forbidden_files)

root_dir = './'
remove_forbidden_items(root_dir, forbidden_dir, forbidden_files)
