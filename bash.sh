"""
create venv
pip install gapi
create alias to run main.py using: booking_system <arg>
"""
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
echo alias wtc-clinic="$PWD/wtc-clinic" >> ~/.bashrc
echo alias wtc-clinic="$PWD/wtc-clinic" >> ~/.zshrc
​
chmod +x wtc-clinic