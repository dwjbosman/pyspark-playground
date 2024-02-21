# Setup env
set HADOOP_CONF_DIR="%HADOOP_HOME%\etc\hadoop"
set PYSPARK_PYTHON=python3  

SET HDFS_NAMENODE_USER=root
SET HDFS_DATANODE_USER=root
SET HDFS_SECONDARYNAMENODE_USER=root
SET YARN_RESOURCEMANAGER_USER=root
SET YARN_NODEMANAGER_USER=root

## get hadoop class path
>hadoop classpath
>set SPARK_DIST_CLASSPATH="C:\Users\dwjbo\hadoop-3.3.5\etc\hadoop";C:\Users\dwjbo\hadoop-3.3.5\share\hadoop\common;C:\Users\dwjbo\hadoop-3.3.5\share\hadoop\common\lib\*;C:\Users\dwjbo\hadoop-3.3.5\share\hadoop\common\*;C:\Users\dwjbo\hadoop-3.3.5\share\hadoop\hdfs;C:\Users\dwjbo\hadoop-3.3.5\share\hadoop\hdfs\lib\*;C:\Users\dwjbo\hadoop-3.3.5\share\hadoop\hdfs\*;C:\Users\dwjbo\hadoop-3.3.5\share\hadoop\yarn;C:\Users\dwjbo\hadoop-3.3.5\share\hadoop\yarn\lib\*;C:\Users\dwjbo\hadoop-3.3.5\share\hadoop\yarn\*;C:\Users\dwjbo\hadoop-3.3.5\share\hadoop\mapreduce\*

# startup

## master

rd /S /Q %HADOOP_HOME%\data\dfs
hdfs namenode -format
start-dfs

In a terminal with admin priv

start-yarn

## worker

start-dfs-datanode
start-yarn-nodemanager

## prepare hdfs

hdfs dfs -mkdir -p /user/spark/share/lib/ 
hdfs dfs -put %SPARK_HOME%\jars\* /user/spark/share/lib/ 
hdfs dfs -mkdir -p /spark-logs    

# Run a job

spark-submit --master yarn --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=C:\Users\dwjbo\Downloads\pyspark-playground-main\pyspark-playground-main\.venv\Scripts\python.exe --conf spark.exectorEnv.PYSPARK_PYTHON=C:\Users\dwjbo\Downloads\pyspark-playground-main\pyspark-playground-main\.venv\Scripts\python.exe --conf spark.yarn.appMasterEnv.PYTHONPATH=C:\Users\dwjbo\Downloads\pyspark-playground-main\pyspark-playground-main\.venv\Lib\site-packages --conf spark.executorEnv.PYTHONPATH=C:\Users\dwjbo\Downloads\pyspark-playground-main\pyspark-playground-main\.venv\Lib\site-packages C:\Users\dwjbo\Downloads\pyspark-playground-main\pyspark-playground\examples\hello_world.py


spark-submit --verbose --master yarn --deploy-mode cluster --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=C:\Users\dwjbo\Downloads\pyspark-playground-main\pyspark-playground-main\.venv\Scripts\python.exe --conf spark.exectorEnv.PYSPARK_PYTHON=C:\Users\dwjbo\Downloads\pyspark-playground-main\pyspark-playground-main\.venv\Scripts\python.exe --conf spark.yarn.appMasterEnv.PYTHONPATH=C:\Users\dwjbo\Downloads\pyspark-playground-main\pyspark-playground-main\.venv\Lib\site-packages --conf spark.executorEnv.PYTHONPATH=C:\Users\dwjbo\Downloads\pyspark-playground-main\pyspark-playground-main\.venv\Lib\site-packages C:\Users\dwjbo\Downloads\pyspark-playground-main\pyspark-playground\examples\hello_world.py 

spark-submit --verbose --master yarn --deploy-mode client --class org.apache.spark.examples.SparkPi C:\Users\dwjbo\spark-3.5.0-bin-hadoop3-scala2.13\examples\jars\spark-examples_2.13-3.5.0.jar 1

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

## Misc

https://www.7-zip.org/

## Java

https://learn.microsoft.com/en-us/java/openjdk/download#openjdk-11
C:\Program Files\Microsoft\jdk-11.0.22.7-hotspot\



## Hadoop
Note unpack haddop and spark with 7-zip with administrative privileges

https://archive.apache.org/dist/hadoop/common/hadoop-3.3.5/

Install in C:\Users\dwjbo\hadoop-3.3.5

### Winutils
Get Winutils
https://github.com/cdarlint/winutils.git

copy the files into the bin folder

try to run winutils.exe, if dll error: 
https://www.microsoft.com/en-US/Download/confirmation.aspx?id=26999 (Visual C++ Redistributable for Visual Studio 2010) (install both x86, x64)

### Configuration

Copy Windows/etc_hadoop/* into hadoop-3.3.5/etc/hadoop
Copy Windows/sbin_hadoop/* to hadoop-3-3.5/sbin

## Spark

https://www.apache.org/dyn/closer.lua/spark/spark-3.5.0/spark-3.5.0-bin-without-hadoop.tgz

### Configuration

Copy Windows/spark_conf/* into spark<XYZ>/conf

## PySPark

Create a venv
pip install -r requirements/requirements.in