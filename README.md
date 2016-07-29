# StageToRemote
### A python module for helping copy stage file to remote server.
If you develop on remote server with git, 
this tool can help you copy staged file to remote server or print scp command

#### Copy file mechanism
At current version, support copy file to remote server (or print scp command) when file status is **staged** 
    

#### Getting Start

setup python libraries

	pip install -r requirement.txt

you can use *--help* to get command information

	$ python app.py --help
	--help: Print help message.
	--version: Print script version.
	--print: Print scp command.
	--auto: Auto copy files to remote server.
	
#### Configuration
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
    
