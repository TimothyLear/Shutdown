# Shutdown
Create Shutdown.py file with -    sudo Shutdow.py

Make script run on boot -          sudo mv Shutdown.py /usr/local/bin/
Make executable    -               sudo chmod +x /usr/local/bin/Shutdown.py

Script to Start/Stop   -           sudo Shutdown.sh

Make script run on boot -           sudo mv Shutdown.sh /etc/init.d/
Make executable -                   sudo chmod +x /etc/init.d/Shutdown.sh

                                    sudo update-rc.d Shutdown.sh defaults
                                     sudo /etc/init.d/Shutdown.sh start
