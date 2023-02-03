# first-ml-project


creating conda environment
'''
conda  create -p venv python==3.7 -y
'''

to activate environment
'''
conda activate venv/
'''

to install all the packege in one time
'''
pip install -r requirements.txt
'''
to add file in github
'''
git add filename
'''
to add all file in github
'''
git add .
'''
those file we dont want to send github
'''
add those file name in .gitnore file
'''
to go on github
'''
git remote -v
'''
to push file in github
'''
git push origin main
'''
to run python file
'''
python app.py
'''
to check sataus which file availble in github

'''
git status
'''
to create Doker file
'''
pip install  docker
'''
BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tagname> .
note: image name for docker must be lowercase
to list docker image
'''
docker images
'''
run docker images
'''
docker run -p 5000:5000 -e PORT =5000 image id
# - p specify port number -e environment variable port
 to check runiing docker container
 '''
 docker ps
 '''
 docker stop <container_id>

