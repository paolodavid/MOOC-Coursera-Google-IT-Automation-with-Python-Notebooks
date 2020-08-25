~$ cat hello_world.txt
Hello World
~$ cat hello_world_long.txt
Hello World

It's a wonderful day!
~$ diff -u hello_world.txt hello_world_long.txt
--- hello_world.txt     2019-12-16 19:24:12.556102821 +0900
+++ hello_world_long.txt        2019-12-16 19:24:38.944207773 +0900
@@ -1 +1,3 @@
 Hello World
+
+It's a wonderful day!
~$ diff -u hello_world.txt hello_world_long.txt > hello_world.diff
~$ patch < hello_world.diff
patching file hello_world.txt
~$ cat hello_world.txt
Hello World

It's a wonderful day!
