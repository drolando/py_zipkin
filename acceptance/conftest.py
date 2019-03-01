import os
import subprocess
import time

import pytest
import requests


ZIPKIN_VERSION = '2.12.6'
RETRIES = 100
WAIT_INTERVAL = 0.1

BINTRAY = 'https://jcenter.bintray.com/io/zipkin/java/zipkin-server'
PATH = '/{version}/zipkin-server-{version}-exec.jar'.format(version=ZIPKIN_VERSION)
URL = BINTRAY + PATH
JAR_NAME = 'zipkin-server-{}.jar'.format(ZIPKIN_VERSION)
JAR_PATH = 'acceptance/{}'.format(JAR_NAME)
JAVA_CMD = 'java -jar {} --logging.level.zipkin2=DEBUG'


@pytest.fixture(autouse=True, scope='module')
def zipkin_server():
    download_zipkin_server()
    proc = subprocess.Popen(JAVA_CMD.format(JAR_PATH), shell=True)
    wait_for_zipkin()
    yield
    proc.kill()


def download_zipkin_server():
    if not os.path.isfile(JAR_PATH):
        jar = requests.get(URL).content
        with open(JAR_PATH, 'wb') as fp:
            fp.write(jar)


def wait_for_zipkin():
    for _ in range(RETRIES):
        try:
            r = requests.get('http://127.0.0.1:9411/health')
            if r.status_code == 200:
                return
        except Exception:
            pass
        time.sleep(WAIT_INTERVAL)
    raise RuntimeError('Zipkin didn\'t start in {} seconds'.format(
        RETRIES * WAIT_INTERVAL,
    ))
