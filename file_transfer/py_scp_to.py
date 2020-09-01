# coding:utf-8
import os, re, sys
import paramiko


def upload(local_path, remote_ip, uname, upasswd, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # ssh.connect('192.168.0.104', 22, 'owhyt', 'oubuntu')
        ssh.connect(remote_ip, port, uname, upasswd)
    except paramiko.ssh_exception.AuthenticationException as passwd_wrong:
        print(passwd_wrong, "远程密码错误")
    except Exception as e:
        print(e)
    else:
        sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())

        remote_path = os.path.join("/home/python_test", os.path.basename(local_path))
        print(remote_path)
        if os.path.isdir(local_path):
            sftp.mkdir(remote_path, os.stat(local_path).st_mode)
            for root, dirs, files in os.walk(local_path):
                for f_name in files:
                    local_file = os.path.join(root, f_name)
                    sm = os.stat(local_file).st_mode
                    relative = local_file.replace(local_path + '/', '')
                    remote_file = os.path.join(remote_path, relative)
                    try:
                        sftp.put(local_file, remote_file)
                        sftp.chmod(remote_file, sm)
                    except Exception as e:
                        print(e)
                        # sftp.mkdir(os.path.dirname(remote_file))
                        # sftp.put(local_file, remote_file)
                    print("upload %s to remote %s" % (local_file, remote_file))
                for f_dir in dirs:
                    local_dir = os.path.join(root, f_dir)
                    sm = os.stat(local_dir).st_mode
                    relative = local_dir.replace(local_path + '/', '')
                    remote_dir = os.path.join(remote_path, relative)
                    try:
                        sftp.mkdir(remote_dir, sm)
                        print("make dir:%s" % remote_dir)
                    except Exception as e:
                        print(e)
            print("INFO: Finished uploading the file/folder %s" % local_path)
        else:
            try:
                sftp.put(local_path, remote_path)
            except Exception as e:
                # print(e)
                raise e
        ssh.close()


upload("/home/owhyt/python_test/transmit_sample.txt", "192.168.0.104", "owhyt", "oubuntu")
