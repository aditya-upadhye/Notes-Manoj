# **`Docker`**
**Docker** is a tool which provides access to run different type of OS in one platform. Which helps to contain and run application in a container. 

A **container** is an isolated environment which runs application with an OS image.
<hr>

> ### Prerequisites to understand this notes

- Basic knowledge about linux and linux commands
- Basic knowledge about ports and protocols
<hr>

> ### Docker vs Virtual Machines
Virtual Machine runs a complete Operating System with OS kernel and OS image for each and every VM individually<br>
Whereas, in docker it uses base OS's kernel for all containers and runs only the image to run the applications.
<hr>

> ### Installation
**Docker Desktop:**<br>
 Windows: https://docs.docker.com/desktop/windows/install/<br>
 Mac: https://docs.docker.com/desktop/mac/install/

**Docker Engine:**<br>
 https://docs.docker.com/engine/install/

<hr>

> ### Docker Commands

#### Starting docker service
To start a docker service
```ps
service docker start
```

To start running the docker while system starts
```
service docker start --enable
```

#### To give permission for current user to use docker with sudo privileges
```ps
sudo gpasswd -a $USER docker
```

#### To list available images in docker

```ps
docker images
```

#### To pull an image

```ps
docker pull [IMAGE_NAME]:[TAG]
```

#### To search for a image in docker hub

```ps
docker search [image_name_query]
```

#### To run a docker image

```ps
docker run -t IMAGE_NAME
```

#### To run a docker image with tag

```ps
docker run -t IMAGE_NAME:TAG
```

> While running `docker run` command without --name will give random name for your container 

#### Running container with name

```ps
docker run --name CONTAINER_NAME_OVER_HERE -t IMAGE:VERSION_TAG
```

#### To run a docker image with detached terminal

```ps
docker run -d --name CONTAINER_NAME_OVER_HERE -t IMAGE:VERSION_TAG
```

**where,**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **-d** is detach container from terminal<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **-t** tty *(TeleTYpewriter)*

#### To execute commands in specific container

```ps
docker exec -it [CONTAINER_NAME] [COMMAND TO BE EXECUTED IN CONTAINER]
```

#### To stop a specific container with name

```ps
docker stop [CONTAINER NAME]
```

#### To stop all container with one command

```ps
docker stop $(docker ps -q)
```

#### To remove all pulled images from docker (READ THE HEADING PROPERLY)
```ps
docker rm $(docker image ls -a -q)
```

#### Port Forwarding in docker
```
docker run -dit --name [CONTAINER NAME] -p [STARTING_PORT]:[END_PORT] [IMAGE NAME]
```
#### List images arguments and aliases (From `docker help`) 
###### List images

**`Aliases:`**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ls, list

**`Options:`**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  -a, --all&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Show all images (default hides intermediate images)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      --digests         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Show digests<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  -f, --filter filter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Filter output based on conditions provided<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      --format string   &nbsp;&nbsp;&nbsp;Pretty-print images using a Go template<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      --no-trunc        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don't truncate output<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  -q, --quiet&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;           Only show image IDs<br>
<hr>


> ### `Dockerfile`
###### Dockerfile syntaxes
```docker
FROM IMAGE:TAG # Similar to import in python Eg: FROM python:latest
ADD FOLDER_TO_COPY_FROM FOLDER_TO_PASTE # Eg: ADD . /root
COPY FOLDER_TO_COPY_FROM FOLDER_TO_PASTE # Similar to ADD 
WORKDIR DIRECTORY_TO_START #similar to cd but it sets the working directory
RUN COMMAND # The command to run on every build
CMD ['EXECUTABLE', 'PARAMETER_1', 'PARAMETER_2'...] # It will run on every time when docker container is created with this image 
ENV [VARNAME]=KEY # Stores env key 
LABEL version="1.0" # LABEL is used to store metadata
MAINTAINER [ORGANIZATION]=AUTHOR # It is deprecated, Since Label can store this data
ARG VARIABLE_TO_IMPORT # similar to FROM but it is for getting value not for image
EXPOSE <port> [<port>/<protocol>...] # Exposes ports to outer machine which runs docker.        
# You need to mention -p to mention its port number
```
Check all other syntaxes on [Dockerfile Reference (OFFICIAL DOCS)](https://docs.docker.com/engine/reference/builder/)

##### To build a image with dockerfile
```ps
docker build .
```

#### To build a image with dockerfile with specified repository name, image name and tag
```ps
docker build -t REPO_NAME/IMAGE_NAME:TAG .
```
<hr>

> ### `.dockerignore` file
###### `.dockerignore` file is similar to `.gitignore`
```docker
# comment    [Ignored line]

*/temp*    # Exclude files and directories whose names start with temp in any 
# immediate subdirectory of the root. 
# For example, the plain file /somedir/temporary.txt is excluded.

*/*/temp* #Exclude files and directories starting with
# temp from any subdirectory, that is two levels below the root/base folder.
# For example, /somedir/subdir/temporary.txt is excluded.

temp? # Exclude files and directories in the root directory
# whose names are a one-character extension of temp.
# For example, /tempa and /tempb are excluded.
```

> #### To create docker image from container
> https://www.sentinelone.com/blog/create-docker-image/
