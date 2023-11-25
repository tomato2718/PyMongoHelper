from json import dumps
from logging import getLogger

from ._argparser import arg_parser

logger = getLogger(__name__)

if __debug__:
    logger.setLevel('DEBUG')
    logger.debug('Running under DEBUG mode.')

if __name__ == '__main__':
    args = arg_parser().parse_args()
    logger.debug(dumps(vars(args), indent=4))