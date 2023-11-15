# Note

## Scrapyd

scrapyd > scrapyd_logs.txt 2>&1 &

### API
To check the load status of a service.
`curl http://localhost:6800/daemonstatus.json`
Schedule a spider run (also known as a job), returning the job id.
`curl http://localhost:6800/schedule.json -d project=bookscraper -d spider=bookspider`

## Scrapy-deploy

scrapyd-deploy default

## Scrapy-web
scrapydweb > scrapydweb_logs.txt 2>&1 &



## Pyenv

export v=3.9.0; wget https://npm.taobao.org/mirrors/python/$v/Python-$v.tar.xz -P ~/.pyenv/cache/; pyenv install $v 

sudo apt-get update
cann't correct install python cause bz2 module missing
- https://stackoverflow.com/questions/60775172/pyenvs-python-is-missing-bzip2-module
