1. Login

	url: aetna.nycdatascience.com
	username: <username>
	password: <password>

2. Open Terminal

3. Start Hadoop
	
	start-hadoop.sh

4. Download data/scripts

	git clone https://github.com/nycdatasci/aetna.git
	cd aetna/
	./setup.sh

You can now start using hadoop.
Afer finishing your work you can release the resources by running the following steps

5. Stop Hadoop
	
	stop-haoop.sh

6. JupyterHub -> Control Panel -> Stop My Server -> Logout
