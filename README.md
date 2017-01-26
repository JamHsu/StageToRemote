# StageToRemote
## A python module for helping copy stage file to remote server.
If you develop on remote server with git, 
this tool can help you copy staged file or specified commit range to remote server or print scp command

### Version
version= 1.1

### Copy file mode
At current version, support below mode
 1. copy file to remote server (or print scp command) when file status
    is **staged**
 2. copy file of **specified commit range** to remote
    server (or print scp command)


### Getting Start

setup python libraries

	pip install -r requirement.txt

you can use *--help* to get command information

	$ python app.py --help
	usage: app.py [-h] (--version | --show | --auto) [-s START_CODE] [-e END_CODE]

	optional arguments:
	  -h, --help            show this help message and exit
	  --version             show the version number
	  --show                print the scp command for all stage file
	  --auto                auto process scp command for all stage file, copy
				files to remote server.
	  -s START_CODE, -start START_CODE
				start commit hash code
	  -e END_CODE, -end END_CODE
				end commit hash code
	
### Configuration
You need configure Repo and SSH infomation in *config.ini* first

    [Repo]
    repo_path={repo_path}
    
    [SSH]
    ip={server_ip}
    user={account}
    password={password}
    
and configure the correlate path in *correlate_path.json*, the script will replace the src to target for full file path

    [
          {
            "name" : {name},
            "src" : {partial src file path},
            "target" : {replace src string to this}
          },
          .....
    ]
    
