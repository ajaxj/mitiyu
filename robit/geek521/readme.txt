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


香港服务器上的mitiyu.sh

#!/bin/bash
cd /home/www/data/py/mitiyu/robit/geek521/
python fetchurl.py