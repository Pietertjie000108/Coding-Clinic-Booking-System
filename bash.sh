CDIR=`readlink -f .`


# pip3 install whirlpool
# pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
# pip3 install rich


alias wtc-clinic="$CDIR/wtc-clinic" >> ~/.bashrc
alias wtc-clinic="$CDIR/wtc-clinic" >> ~/.zshr


chmod +x wtc-clinic


echo $CDIR