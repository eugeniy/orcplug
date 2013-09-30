import logging

log = logging.getLogger('orc.plugin.%s' % __name__)


def api_handler():
    return 'hello, plugin handler!'


def custom_logger():
    return 'hello, plugin logger!'
