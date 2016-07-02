import logging
import logging.handlers


class LogConfiguration:
    """
    This class handles common logging options for the entire project
    """
    def __init__(self, filename, debug=False):
        # create console handler
        self._consoleLogger = logging.StreamHandler()
        self._consoleLogger.setFormatter(logging.Formatter(
            '[%(levelname)s] %(message)s'))
        if debug:
            self._consoleLogger.setLevel(logging.DEBUG)
        else:
            self._consoleLogger.setLevel(logging.INFO)
        # create a file handler
        self._fileLogger = logging.handlers.RotatingFileHandler(
            'logs/%s.log' % filename,
            maxBytes=1024*1024,  # 1 Mb
            backupCount=20)
        self._fileLogger.setLevel(logging.DEBUG)
        # create a logging format
        formatter = logging.Formatter(
            '[%(name)s][%(levelname)s][%(asctime)s] %(message)s')
        self._fileLogger.setFormatter(formatter)

    @property
    def file_logger(self):
        return self._fileLogger

    @property
    def console_logger(self):
        return self._consoleLogger

    def create_logger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        # add the handlers to the logger
        logger.addHandler(self.file_logger)
        logger.addHandler(self.console_logger)
        return logger