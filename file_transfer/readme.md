- 脚本用于通信的两台主机之间的文件或目录传输，用Python的paramiko模块实现scp命令的效果。
- The script, using Python's paramiko module to achieve the effect of scp command, is used to transfer files or directories between two hosts that communicate.
1. py_scp_to.py
	用于将本地文件或目录传送到远程主机。
2. py_scp_from.py
 	用于将远程主机上的文件目录传送到本地。
3. 待优化点或问题点
1) py_scp_to.py脚本：拷贝本地目录到远程主机某一目录时，远程目录下存在相同命名的文件夹时，并不会覆盖，且会报错。
2）py_scp_to.py脚本：远程目录没有是写死的固定目录，需要安排一个参数。
3) py_scp_from.py脚本也存在上述的两个问题。

