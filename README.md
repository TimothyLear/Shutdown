# shutdown
Create Shutdown.py file with     
    sudo shutdow.py

Make script run on boot
    sudo mv shutdown.py /usr/local/bin/
Make executable    
    sudo chmod +x /usr/local/bin/shutdown.py

Script to Start/Stop   
    sudo shutdown.sh

Make script run on boot   
    sudo mv shutdown.sh /etc/init.d/
Make executable 
    sudo chmod +x /etc/init.d/shutdown.sh

    
    sudo update-rc.d shutdown.sh defaults
    sudo /etc/init.d/shutdown.sh start
