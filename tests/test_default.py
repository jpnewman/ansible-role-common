"""Common Install Specs."""

import testinfra.utils.ansible_runner
import re

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_python_package(host):
    """Test Python is installed."""
    python = host.package('python')
    assert python.is_installed


def testsoftware_properties_common_package(host):
    """Test software_properties_common packages are installed."""
    software_properties_common = host.package('software-properties-common')
    assert software_properties_common.is_installed


def test_vim_package(host):
    """Test vim packages are installed."""
    vim = host.package('vim')
    assert vim.is_installed


def test_htop_package(host):
    """Test htop packages are installed."""
    htop = host.package('htop')
    assert htop.is_installed


def test_alternative_editor(host):
    """Test alternative editor."""
    alternative_editor = host.command('ls -lha /etc/alternatives/editor')
    assert '/usr/bin/vim.tiny' in alternative_editor.stdout


def test_bash_aliases(host):
    """Test bash aliases."""
    bash_aliases = host.file('/etc/skel/.bash_aliases')
    assert bash_aliases.contains('alias ll="ls -l"')
    assert bash_aliases.contains('alias la="ls -lha"')


def test_limits_conf_file(host):
    """Test limit."""
    limits_conf_content = host.file('/etc/security/limits.conf')

    hard_pattern = re.compile(r"^\s*\*\s+hard\s+nofile\s+unlimited\s*$", re.IGNORECASE | re.MULTILINE)
    assert re.search(hard_pattern, limits_conf_content.content_string)

    soft_pattern = re.compile(r"^\s*\*\s+soft\s+nofile\s+unlimited\s*$", re.IGNORECASE | re.MULTILINE)
    assert re.search(soft_pattern, limits_conf_content.content_string)


def test_pam_limits_so(host):
    """Test pam limits."""
    expected_line = 'session    required    pam_limits.so'

    pam_d_su = host.file('/etc/pam.d/su')
    assert pam_d_su.contains(expected_line)

    common_session = host.file('/etc/pam.d/common-session')
    assert common_session.contains(expected_line)

    common_session_noninteractive = host.file('/etc/pam.d/common-session-noninteractive')
    assert common_session_noninteractive.contains(expected_line)

    pam_d_sudo = host.file('/etc/pam.d/sudo')
    assert pam_d_sudo.contains(expected_line)
