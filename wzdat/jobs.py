import logging

import argh

from wzdat.make_config import make_config
from wzdat.ipynb_runner import update_notebook_by_run
from wzdat.rundb import get_cron_notebooks, cache_files, cache_finder,\
    save_cron
from wzdat.util import gen_dummydata as _gen_dummydata


cfg = make_config()


def cache_all():
    logging.debug('cache_all')
    cache_files()
    cache_finder()


def register_cron():
    from wzdat.util import get_notebook_dir
    from wzdat.ipynb_runner import find_cron_notebooks, register_cron_notebooks
    nb_dir = get_notebook_dir()
    paths, scheds, _, _ = find_cron_notebooks(nb_dir)
    logging.debug("register_cron")
    register_cron_notebooks(paths, scheds)
    save_cron(paths, scheds)


def run_all_cron_notebooks():
    logging.debug('run_all_cron_notebooks')
    for nbpath in get_cron_notebooks():
        run_notebook(nbpath)


@argh.arg('path', help="notebook path")
def run_notebook(path):
    path = path.decode('utf-8') if type(path) == str else path
    logging.debug(u'run_notebook {}'.format(path))
    update_notebook_by_run(path)


@argh.arg('-d', '--dir', help="target directory where dummy data will be"
          "written into. if skipped, cfg['data_dir'] will be chosen.")
def gen_dummydata(**kwargs):
    td = kwargs['dir']
    if td is None:
        td = cfg['data_dir']
    return _gen_dummydata(td)


@argh.arg('-e', '--type', help="event type")
@argh.arg('-i', '--info', help="event info")
def register_event(**kwargs):
    etype = kwargs['type']
    einfo = kwargs['info']
    print etype, einfo


if __name__ == "__main__":
    argh.dispatch_commands([cache_all, register_cron, run_notebook,
                            gen_dummydata, run_all_cron_notebooks,
                            register_event])
