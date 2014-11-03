import pytest

from wzdat.make_config import make_config
from ws_mysol.myprj import log as l


cfg = make_config()


@pytest.fixture(scope="session")
def dummy():
    from wzdat.util import gen_dummydata
    gen_dummydata(cfg['data_dir'])


def test_dummy(dummy):
    assert len(l.files) > 0
