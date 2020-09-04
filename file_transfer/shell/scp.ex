#!/usr/bin/expect
# 设置半小时超时间
set timeout 1800

if {[llength $argv] < 3} {
    puts "$argv0 local_file remote_path"
    exit 1
}
set local_file [lindex $argv 0]
set remote_path [lindex $argv 1]
set passwd [lindex $argv 2]
set passwderror 0
spawn scp -r $local_file $remote_path
expect {
    "*assword*" {
        if {$passwderror == 1} {
            puts "passwd is error"
            exit 2
        }
        set timeout 600
        set passwderror 1
        send "$passwd\r"
        exp_continue
    }
    "*es/no*" {
        send "yes\n"
        exp_continue
    }
    timeout {
        puts "connection is timeout"
        exit 3
    }
}


