#pylogagent简介
**pylogagent**是基于[pysvrkit](https://github.com/jackdai123/pysvrkit)开发的python日志服务，主要解决如下问题：
- **多进程logging** ：python标准库logging是一个进程不安全（但线程安全）的库，即多进程服务写日志会打到多个日志文件，不方便查看；
- **多服务日志文件** ：使用默认logging库，多个服务（尤其是微服务）会打到多个日志文件，导致磁盘IO增高；

#启动pylogagent服务
- git clone https://github.com/jackdai123/pylogagent.git
- cd pylogagent
- cat logagent_svr.conf
```ini
[app]
name=logagent
pid=/tmp/logagent.pid

[rpc_server]
ip=0.0.0.0
port=4000
worker_type=thread
worker_sum=4

[loggers]
keys=root

[logger_root]
level=DEBUG
handlers=logagent

[handlers]
keys=logagent

[handler_logagent]
class=handlers.TimedRotatingFileHandler
formatter=logagent
args=('/tmp/logagent', 'h', 1, 24)

[formatters]
keys=logagent

[formatter_logagent]
format=%(asctime)s [%(levelname)s] %(message)s
datefmt=%Y-%m-%d %H:%M:%S
```
- ./logagent start
- ps -ef | grep logagent
```bash
vagrant  16469     1  0 05:31 ?        00:00:00 python /home/vagrant/pylogagent/logagent_svr.py -f /home/vagrant/pylogagent/logagent_svr.conf -d
vagrant  16484  3582  0 05:31 pts/0    00:00:00 grep --color=auto logagent
```
- cat logagent_cli.conf
```ini
[server]
sum=1
mode=hashring

[server0]
ip=127.0.0.1
port=4000
weight=100
```
- cat logagent_test.py
```python
def test_critical():
        cli = logagent_cli.Client('logagent_cli.conf', modulename='logagent_test')
        cli.critical('%s %d', 'test_critical', 123)
```
- python logagent_test.py
- cat /tmp/logagent
```
2016-07-25 05:34:23 [CRITICAL] [logagent_test] test_critical 123
```
- ./logagent stop

#依赖库
- [msgpackrpc](https://github.com/msgpack-rpc/msgpack-rpc-python)
- [daemonize](https://github.com/thesharp/daemonize)
- [gevent](https://github.com/gevent/gevent)
- [consistent_hash](https://github.com/yummybian/consistent-hash)


# 反馈与建议
- 微信：david_jlu
- QQ：26126441
- 邮箱：<david_jlu@foxmail.com> 
