from utils.logger import get_logger


logger = get_logger(__name__)


def test_logger():

    logger.info("开始执行日志测试")

    logger.info("这是一条 INFO 日志")

    logger.warning("这是一条 WARNING 日志")

    logger.error("这是一条 ERROR 日志")

    assert True

    logger.info("日志测试完成")