# Setup env
set HADOOP_CONF_DIR="%HADOOP_HOME%\etc\hadoop"
set PYSPARK_PYTHON=python3  

SET HDFS_NAMENODE_USER=root
SET HDFS_DATANODE_USER=root
SET HDFS_SECONDARYNAMENODE_USER=root
SET YARN_RESOURCEMANAGER_USER=root
SET YARN_NODEMANAGER_USER=root

# starup

rd /S /Q %HADOOP_HOME%\data\dfs
hdfs namenode -format

# Some commands to remember
jps
hdfs namenode -format
yarn node -list

%HADOOP_HOME%\sbin\start-dfs.cmd

Needs administrator priv:
%HADOOP_HOME%\sbin\start-yarn.cmd
%HADOOP_HOME%\sbin\stop-yarn.cmd

http://localhost:8088/cluster
http://localhost:9870/dfshealth.html#tab-overview

# Env variables via control panel

HADOOP_HOME=C:\Users\dwjbo\hadoop-3.3.5
SPARK_HOME=C:\Users\dwjbo\spark-3.5.0-bin-without-hadoop

PATH:
%SPARK_HOME%\bin
%HADOOP_HOME%\bin
%HADOOP_HOME%\sbin
%SPARK_HOME%\sbin
%HADOOP_HOME%\lib\native

# SSH installation

Set-Service -Name sshd -StartupType 'Automatic'
icacls $env:USERPROFILE\.ssh /reset /T /C /Q
icacls $env:USERPROFILE\.ssh /grant:r "${env:USERNAME}:R" /T /C /Q
icacls $env:USERPROFILE\.ssh\authorized_keys /grant:r "${env:USERNAME}:R" /T /C /Q
icacls $env:USERPROFILE\.ssh /grant:r "${env:USERNAME}:(OI)(CI)(F)" /T /C /Q
icacls $env:USERPROFILE\.ssh\authorized_keys /grant:r "${env:USERNAME}:W" /T /C /Q
Restart-Service sshd

# Packages

C:\Program Files\Microsoft\jdk-11.0.22.7-hotspot\