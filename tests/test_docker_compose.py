import re
from pathlib import Path

def read_compose():
    return Path('docker-compose.yml').read_text()

def test_services_defined():
    content = read_compose()
    assert 'backend:' in content, 'backend service missing'
    assert 'frontend:' in content, 'frontend service missing'

def test_backend_port_mapping():
    content = read_compose()
    # look for the exact port mapping line
    pattern = re.compile(r"^\s*-\s*'5001:5000'", re.MULTILINE)
    assert pattern.search(content), 'backend port mapping 5001:5000 not found'
