#/bin/bash

sudo cp -r ./data3 /mnt
sudo ln -s /mnt/data3 /data3
/mnt/data3/db-init.sh
