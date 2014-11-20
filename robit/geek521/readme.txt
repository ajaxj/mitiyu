//参考阿里云里面的配置

crontab -l
* 7 * * * /home/mitiyu.sh
mitiyu.sh
#!/bin/bash
cd /home/env/
source ./bin/activate
cd /home/www/myrobit/mitiyu/
/home/env/bin/python fetch8bobs.py
/home/env/bin/python fetch8bo.py
deactivate


/mnt/data/mitiyu.sh
#!/bin/bash
cd /mnt/data/pyenv/
source ./bin/activate
cd /home/www/data/py/mitiyu/robit/geek521/
/home/www/data/pyenv/bin/python fetchurl.py
deactivate
