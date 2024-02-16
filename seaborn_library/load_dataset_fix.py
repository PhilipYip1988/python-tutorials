import seaborn as sns
import io
import os
import requests
import shutil
import zipfile

# Get data folder
data_dir = sns.get_data_home()

# Delete old data folder
shutil.rmtree(data_dir)

# Recreate data folder
os.mkdir(data_dir)

# Download
r = requests.get('https://codeload.github.com/mwaskom/seaborn-data/zip/refs/heads/master')
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall(path=data_dir)

# Move contents from extracted folder to parent directory
download_dir = os.path.join(data_dir, 'seaborn-data-master')

files = os.listdir(download_dir)

for filename in files:
    old_file_name = os.path.join(data_dir, 'seaborn-data-master', filename)
    new_file_name = os.path.join(data_dir, filename)
    shutil.move(old_file_name, new_file_name)
os.rmdir(download_dir)
