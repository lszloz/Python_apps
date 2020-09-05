#!/usr/bin/expect
set num [lindex $argc]
spawn echo $num
set timeout 1800
set host [lindex $argv 0]
set username [lindex $argv 1]
set password [lindex $argv 2]
set cmd [lindex $argv 3]
set uname_nested [lindex $argv 4]

spawn echo $cmd
spawn ssh $username@$host
expect {
    "*yes/no*" {send "yes\n";exp_continue}
    "*assword*" {send "$password\n"}
    "#" {send "\n"}
}
if {$argc == 5} {
    send "su - $uname_nested\n"
    expect {
        "*assword:" {send "password\n"}
    }
}
send "$cmd\n"
if {$argc == 5} {
    send "exit\n"
}
send "exit\n"
expect eof
