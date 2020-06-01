# BiologyLabWeb

# Running the Website

1. make sure you have python installed.
2. run `pip install -r requirements.txt`.
3. run `make` if you are contributing; run `make production` if you are deploying.
4. open your browser and go to `localhost:5000` or the domain you bind with.

# Configurations

If you decide to host your own website, you will need to change the `config.json`
accordingly. Remember that if you are developing the application, you should never
commit sensitive informations in the `config.json` in the version control system.

# Changing Content

By default, the articles at `localhost:5000` is an example of Markdown style document,
you will need to go to `BiologyLabWeb/content/` and change them correspondently.