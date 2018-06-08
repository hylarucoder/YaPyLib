from yapylib.logging import get_logger


def test_get_logger():
    get_logger().debug("测试 DEBUG ")
    get_logger().info("测试 INFO ")
    get_logger().critical("测试 CRITICAL ")
    get_logger().error("测试 ERROR ")
    assert True == True
