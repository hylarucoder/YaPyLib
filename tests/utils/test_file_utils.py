import os
import pytest


@pytest.fixture
def setup_root_path(tmpdir):
    root_path = str(tmpdir)
    os.makedirs(root_path + "/images/皇后大道东")
    os.makedirs(root_path + "/css/啦啦啦")
    os.makedirs(root_path + "/misc")
    return root_path
