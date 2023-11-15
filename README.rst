=============
ckanext-heroslideradmin
=============

Adds a hero slider to the homepage which can be managed from the sysadmin panel.


------------------------
Development Installation
------------------------

To install ckanext-heroslideradmin for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/OpenGov-OpenData/ckanext-heroslideradmin.git
    cd ckanext-heroslideradmin
    python setup.py develop
    pip install -r dev-requirements.txt

Add heroslideradmin to the ckan.plugins setting in your CKAN config file (by default the config file is located at /etc/ckan/default/production.ini)::

    ckan.plugins = heroslideradmin



---------------
Config Settings
---------------

Run the following command to create the necessary tables in the database (ensuring the pyenv is activated)

ON CKAN >= 2.9::

    (pyenv) $ ckan --config=/etc/ckan/default/production.ini heroslideradmin initdb

ON CKAN <= 2.8::

    (pyenv) $ paster --plugin=ckanext-heroslideradmin heroslideradmin initdb --config=/etc/ckan/default/production.ini

Finally, restart CKAN to have the changes take affect::

    sudo service apache2 restart



-------------------
Hero Slider Snippet
-------------------

To add the hero slider to the homepage, add the following block to the appropriate homepage template (eg: layout3.html)::

    {% snippet 'home/snippets/hero_slider.html' %}
