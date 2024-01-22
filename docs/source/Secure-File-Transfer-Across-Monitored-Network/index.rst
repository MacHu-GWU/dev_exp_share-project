Secure File Transfer Across Monitored Network
==============================================================================
在特殊情况下, 你可能必须要在不可信的机器上需要传送文件. 而这个机器所在的网络可能会有监控软件能对你的网络流量抓包分析, 从而看到内容. 又或者通过防火墙限制了一些传输文件的网络服务. 那这个情况下要怎么做才安全呢?

我的解决案有以下几个要点:

1. 利用 AWS S3 作为中转媒介. 它支持 encryption at transit and at rest. 在网络传输过程和存储中都是加密的.
2. 使用 `windtalker <https://github.com/MacHu-GWU/windtalker-project>`_ Python 库做客户端加密, 保证文件在发送之前就已经被加密了.
3. 密钥在命令行输入, 不留记录. 本地机器的网络监控只知道你把文件上传到 S3 了, 但并不知道内容是什么, 截取了内容也无法解密. AWS S3 本身就算拿到数据也不知道压缩包的内容是什么.

.. dropdown:: Secure file transfer app Python library app.py

    .. literalinclude:: ./app.py
       :language: python
       :linenos:


.. dropdown:: Example usage of app.py

    .. literalinclude:: ./example.py
       :language: python
       :linenos:

