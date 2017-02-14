#!/usr/bin/env bash

cat << EndOfMessage
01) 开发 - 本地机器 - 开启Mac上本地开发环境\n
02) 测试 - 本地机器 - 测试,lint代码质量,覆盖率\n
03) 发布 - PyPi - 发布当前的YaPyLib到PyPi, 并同步当前的项目到Github和Coding\n
EndOfMessage

# set rental to Unknown
if [ -z $1 ]
then
    echo -e "====>> : \c"
    read choice
elif [ -n $1 ]
then
    choice="$1"
fi

start=`date +%s`
case "$choice" in
    01) echo "开发 - 本地机器 - 开启Mac上本地开发环境"
       ;;
    02) echo "测试 - 本地机器 - 测试,lint代码质量,覆盖率"
       ;;
    03) echo "发布 - PyPi - 发布当前的YaPyLib到PyPi, 并同步当前的项目到Github和Coding"
       ;;
    *) echo "无此选项"
       ;;
esac
end=`date +%s`

runtime=$((end-start))

echo "本脚本执行时间为：$runtime s"

