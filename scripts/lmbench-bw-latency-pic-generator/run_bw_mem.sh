
# 循环调用 1K, 16K, 32K, 64K, 128K, 256K, 512K, 1M, 2M, 4M, 8M, 16M, 32M, 64M, 128M, 256M, 512M
for size in 1K 16K 32K 64K 128K 256K 512K 1M 4M 16M 32M 64M 128M 256M 512M
do
    adb shell "taskset 80 /data/local/tmp/bw_mem $size rd" 2<&1 | tee bw_mem_rd_$size.log
done