#!/bin/bash

file=$1

for i in {0..100000};
do
    if [[ $file == *"zip"* || $file == *"kz3"* ]];then
        echo $file;
        unzip $file;
        cd "$i";
        file=`ls|grep -v txt`;
        cat $i.txt>>"~/Downloads/tjctf_2020/Misc/flags";
    else
        echo $file;
        tar -xvf $file;
        cd "$i";
        file=`ls|grep -v txt`;
        cat $i.txt>>"~/Downloads/tjctf_2020/Misc/flags";
    fi
done;
