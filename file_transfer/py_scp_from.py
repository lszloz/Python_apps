import paramiko
import os
from stat import S_ISDIR


def recur_down(remote_cur_path, local_path, sftp):
    folders = [f.filename for f in sftp.listdir_attr(remote_cur_path) if S_ISDIR(f.st_mode)]
    files = [f.filename for f in sftp.listdir_attr(remote_cur_path) if not S_ISDIR(f.st_mode)]
    if files:
        for file in files:
            try:
                local_file = os.path.join(local_path, file)
                remote_file = os.path.join(remote_cur_path, file)
                sm = sftp.stat(remote_file).st_mode
                sftp.get(remote_file, local_file)
                os.chmod(local_file, sm)
            except IOError as e:
                print("[ERROR] Remote_path or local_path doesn't exist.")
    if folders:
        for folder in folders:
            local_son_folder = os.path.join(local_path, folder)
            remote_son_folder = os.path.join(remote_cur_path, folder)
            sm = sftp.stat(remote_son_folder).st_mode
            os.mkdir(local_son_folder, sm)
            recur_down(remote_son_folder, local_son_folder, sftp)


def download(remote_path, remote_ip, remote_uname, remote_upasswd, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(remote_ip, port, remote_uname, remote_upasswd)
    local_path = os.path.join("/home/user", os.path.basename(remote_path))
    print(local_path)
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    # 若远程path为目录
    st = sftp.stat(remote_path)
    if S_ISDIR(st.st_mode):
        os.makedirs(local_path, st.st_mode)
        recur_down(remote_path, local_path, sftp)
    # 若远程path为文件
    else:
        try:
            sftp.get(remote_path, local_path)
        except Exception as e:
            print(e)
    ssh.close()


# download("/home/python_test/aa", "192.168.1.1", "username", "userpasswd")
download("/home/python_test/transmit_sample.txt", "192.168.1.1", "username", "userpasswd")
