import pytest
import testinfra

# get check_output from local host
check_output = testinfra.get_host("local://").check_output


@pytest.fixture
def host(request):
    # Start a container
    docker_id = check_output("docker run --entrypoint='' -d %s tail -f /dev/null", request.param)

    # yield a dynamic created host
    yield testinfra.get_host("docker://" + docker_id)

    # destroy the container
    check_output("docker rm -f %s", docker_id)


def pytest_generate_tests(metafunc):
    if "host" in metafunc.fixturenames:
        # Lookup "docker_images" marker
        marker = getattr(metafunc.function, "docker_images", None)
        if marker is not None:
            images = marker.args
        else:
            # Default image
            images = ["teknoradio/youtube:latest"]

        if getattr(metafunc.function, "destructive", None) is not None:
            scope = "function"
        else:
            scope = "session"

        metafunc.parametrize("host", images, indirect=True, scope=scope)
