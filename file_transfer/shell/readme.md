1. scp.ex脚本使用
    该脚本用于主机间相互传送文件，可用于自动化脚本中 

    1. 本地文件拷到远程
    
       expect scp.ex  example.txt  user@192.168.1.1:/home/user  password
    
    2. 远程文件拷到本地
    
       expect scp.ex  user@192.168.1.1:/home/user/example  ./  password
    
2. remote_cmd.ex脚本使用

    该脚本用于登录远程主机，并执行一条linux操作系统命令

    expect remote_cmd.ex  192.168.1.1  user  password  'command'

