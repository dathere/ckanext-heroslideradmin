# ckanext-heroslideradmin

Adds a hero slider to the homepage which can be managed from the sysadmin panel.

-------------------
Functionality
-------------------

The end user can either upload their own images or link them as hero sliders on the homepage. The system administrator can add/remove images in the `sytemadmin settings` -> `Hero Slider Config` where is possible to manage hero slided.
The following image shows how the user interface looks like.


![image](https://github.com/user-attachments/assets/78bf0209-08e0-42a3-a94f-614983492758)


The updated images are going to be displayed in the main page. The following images shows the example of the main page.

![image](https://github.com/user-attachments/assets/fe25c698-0b57-4568-b3c4-8e8495a98751)


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

To add the hero slider to the homepage, add the following block to the appropriate homepage template (eg: ckanext-example_plugin/ckanext/example_plugin/templates/home/layout3.html):

    {% if 'heroslideradmin' in g.plugins %} 
        {% snippet 'home/snippets/hero_slider.html' %} 
    {% endif %}



