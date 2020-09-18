# BiologyLabWeb

## Introduction

This website is developed for [Yin's Lab](http://bcb.unl.edu/) located at the [University of Nebraska - Lincoln](https://www.unl.edu) and founded by [NSF](https://www.nsf.gov/).

## Installation

1. Make sure you have python3 and python3-pip installed.
2. Make sure you have clone the website and ready to deploy.
3. run `pip3 install -r requirements.txt` to install all the requirement.
4. We recommand to serve pn Nginx, but here is the instruction: [Instruction to serve on nginx](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04); [Instruction to serve on Apache](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps). 

## Testing and Contributing
1. run `make` if you are contributing; run `make production` if you are deploying.
2. open your browser and go to `localhost:5000` or the domain you bind with.

# Configurations

If you decide to host your own website, you will need to change the `config.json.example` to `config.json` and change configurations accordingly. Remember that if you are developing the application, you should nevercommit sensitive informations in the `config.json` in the version control system.

# Changing Content

By default, the articles at `localhost:5000` is an example of Markdown style document,
you will need to go to `BiologyLabWeb/content/` and change them correspondently.
