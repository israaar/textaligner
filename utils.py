import os
import logging
import logging.handlers
import os.path


def setup_logger():
    if True:
        this_app_base_dir = os.path.abspath(os.path.dirname(__file__))
        log_dir = os.path.join(this_app_base_dir, 'logs')
    else:
        log_dir = os.path.expanduser('~/logs')
    try:
        os.mkdir(log_dir)
    except Exception:
        pass
    log_file = os.path.join(log_dir, 'bilingua.txt')
    handler = logging.handlers.RotatingFileHandler(log_file, "a",
                        encoding="utf-8", maxBytes=1024*512, backupCount=20)
    formatter = logging.Formatter('%(asctime)s %(levelname)5s: %(thread)d [%(filename)14s:%(lineno)d] %(message)s')
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)


def main():
    pass

if __name__ == '__main__':
    main()
