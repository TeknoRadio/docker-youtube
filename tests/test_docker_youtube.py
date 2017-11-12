

def test_that_container_is_running(host):
    assert host.process.get(pid=1).comm == "tail"


def test_that_container_is_ubuntu_xenial(host):
    assert host.system_info.distribution == "ubuntu"
    assert host.system_info.release == "16.04"
    assert host.system_info.codename == "xenial"


def test_that_ffmpeg_is_installed(host):
    assert host.exists('ffmpeg')


def test_that_user_is_added_and_homedir_exists(host):
    user = host.user('user')
    assert user.home == '/home/user'

    homedir = host.file('/home/user')
    assert homedir.is_directory
    assert homedir.user == user.name


def test_that_entrypoint_is_present_and_executable(host):
    script = host.file('/home/user/entrypoint.sh')
    assert script.is_file
    assert script.user == 'user'
    assert script.group == 'nogroup'




