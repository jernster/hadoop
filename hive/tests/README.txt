In HDP 2.5 TP authorization is provided through Ranger resulting in an error similar to below:

hive> SHOW DATABASES;
FAILED: RuntimeException java.io.FileNotFoundException: /etc/hive/2.5.0.0-817/0/xasecure-audit.xml (No such file or directory)

To get around this, in Ambari => Hive Config => Select None for Authorization under the security section.  Restart Hive.
