import subprocess


def simple_command(cmd):
    """
    :param cmd:
    :return:
    简单执行命令行,并且传回
    """
    if isinstance(cmd, list):
        cmd = " ".join(cmd)
    out_bytes = subprocess.check_output(cmd, shell=True, timeout=5, stderr=subprocess.STDOUT)
    if out_bytes:
        out_text = out_bytes.decode('utf-8')
        return out_text
