[program:torsion_shop]
command=/home/agrat/public_html/venv/bin/gunicorn torsion_b2b.wsgi:application -c /home/agrat/public_html/torsion_b2b/config/gunicorn.conf.py
directory=/home/agrat/public_html/torsion_b2b
user=agrat
autorestart=true
redirect_stderr=true
stdout_logfile = /home/agrat/public_html/torsion_b2b/logs/debug.log