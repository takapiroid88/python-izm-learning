import os

# os.path.join
project_dir = 'C:\\python-izm'
settings_file = 'settings.ini'

print(os.path.join(project_dir, settings_file))
print(os.path.join(project_dir, "setting_dir", settings_file))


