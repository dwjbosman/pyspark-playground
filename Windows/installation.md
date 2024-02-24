# SSH installation

Set-Service -Name sshd -StartupType 'Automatic'
icacls $env:USERPROFILE\.ssh /reset /T /C /Q
icacls $env:USERPROFILE\.ssh /grant:r "${env:USERNAME}:R" /T /C /Q
icacls $env:USERPROFILE\.ssh\authorized_keys /grant:r "${env:USERNAME}:R" /T /C /Q
icacls $env:USERPROFILE\.ssh /grant:r "${env:USERNAME}:(OI)(CI)(F)" /T /C /Q
icacls $env:USERPROFILE\.ssh\authorized_keys /grant:r "${env:USERNAME}:W" /T /C /Q
Restart-Service sshd

# Packages

## Scala

https://www.scala-lang.org/download/2.13.12.html

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

copy the files for specific hadoop version (3.3.5) into the bin folder of hadoop (%HADOOP_HOME%\bin)

try to run winutils.exe, if dll error: 
https://www.microsoft.com/en-US/Download/confirmation.aspx?id=26999 (Visual C++ Redistributable for Visual Studio 2010) (install both x86, x64)

### Configuration

Copy Windows/etc_hadoop/* into hadoop-3.3.5/etc/hadoop
Copy Windows/sbin_hadoop/* to hadoop-3-3.5/sbin

## Spark

https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3-scala2.13.tgz

Extract as administrator

### Configuration

Copy Windows\spark_conf\* into %SPARK_HOME%\conf

Rename templates by removing .template

update spark-defaults.conf, specify hadoop.home.dir correctly (escape \)
Note. When setting HADOOP_HOME as a system env var, it will use that variable, however backslashes are not correctly escaped then!

## PySPark

Create a venv
pip install -r requirements/requirements.in

# Env variables via control panel

Have all been set as USER env vars (not SYSTEM)

HADOOP_HOME=C:\Users\dwjbo\hadoop-3.3.5
SPARK_HOME=C:\Users\dwjbo\spark-3.5.0-bin-hadoop3-scala2.13
HADOOP_CONF_DIR=C:\Users\dwjbo\hadoop-3.3.5\etc\hadoop
PYSPARK_PYTHON=python3  

HDFS_NAMENODE_USER=root
HDFS_DATANODE_USER=root
HDFS_SECONDARYNAMENODE_USER=root
YARN_RESOURCEMANAGER_USER=root
YARN_NODEMANAGER_USER=root

PATH:
%SPARK_HOME%\bin
%SPARK_HOME%\sbin
%HADOOP_HOME%\bin
%HADOOP_HOME%\sbin
%HADOOP_HOME%\lib\native

## Setup JAVA_HOME 
(system env var)

C:\Program Files\Microsoft\jdk-11.0.22.7-hotspot\
-> (to avoid spaces)
C:\Progra~1\Microsoft\jdk-11.0.22.7-hotspot\


## get hadoop class path

Not needed

>hadoop classpath
>set SPARK_DIST_CLASSPATH=<hadoop classpath>

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


