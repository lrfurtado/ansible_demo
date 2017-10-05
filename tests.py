import pytest
import testinfra

@pytest.mark.parametrize("name,version", [
    ("nginx", "1.10.2"),
    ("python", "2.7"),
    ("memcached","1.4.15"),
    ("mariadb", "5.5.56"),
    ("nodejs", "6.11.3")
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)

def test_services(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

    mysql = host.service("mariadb")
    assert mysql.is_running
    assert mysql.is_enabled

    memcached = host.service("memcached")
    assert memcached.is_running
    assert memcached.is_enabled

    app = host.service("challenge-app")
    assert app.is_running
    assert app.is_enabled

def test_integration(host):
    stdout = host.check_output("curl localhost")
    assert  'MySQL' in stdout or 'Memcache' in stdout
    stdout = host.check_output("curl localhost")
    assert  'MySQL' in stdout or 'Memcache' in stdout
    stdout = host.check_output("curl localhost")
    assert  'MySQL' in stdout or 'Memcache' in stdout
    stdout = host.check_output("curl localhost")
    assert  'MySQL' in stdout or 'Memcache' in stdout

